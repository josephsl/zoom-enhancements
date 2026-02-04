# zoom.py
# A part of zoomEnhancements add-on
# This file is covered by the GNU General Public License
# See the file COPYING for more details

from nvdaBuiltin.appModules.zoom import AppModule as CoreAppModule
import eventHandler
import tones
from scriptHandler import script
import ui
import config
import addonHandler
from .dialogs import ZoomEnhancementsSettingsPanel, ChatHistoryDialog
from . import regexs
import datetime
import gui
from gui import NVDASettingsDialog
import controlTypes


def initConfiguration():
	confspec = {
		"alertsReportingMode": "string(default=Custom)",
		"ParticipantHasJoined/LeftMeeting": "boolean(default=True)",
		"ParticipantHasJoined/LeftWaitingRoom": "boolean(default=True)",
		"AudioMutedByHost": "boolean(default=True)",
		"VideoStoppedByHost": "boolean(default=True)",
		"ScreenSharingStarted/StoppedByParticipant": "boolean(default=True)",
		"RecordingPermissionGranted/Revoked": "boolean(default=True)",
		"PublicIn-meetingChatReceived": "boolean(default=True)",
		"PrivateIn-meetingChatReceived": "boolean(default=True)",
		"In-meetingFileUploadCompleted": "boolean(default=True)",
		"HostPrivilegeGranted/Revoked": "boolean(default=True)",
		"ParticipantHasRaised/LoweredHand": "boolean(default=True)",
		"RemoteControlPermissionGranted/Revoked": "boolean(default=True)",
		"IMChatReceived": "boolean(default=True)",
	}
	config.conf.spec["zoomEnhancements"] = confspec


# Execute on init
addonHandler.initTranslation()


# Translators: the name of the add-on category in input gestures
SCRCAT_ZOOMENHANCEMENTS = _("Zoom Enhancements")


# Alert reporting mode to label dict
alertModeToLabel = {
	# Translators: a label for alerts reporting mode
	0: _("Report all alerts"),
	# Translators: a label for alerts reporting mode
	1: _("Beep for alerts"),
	# Translators: a label for alerts reporting mode
	2: _("Silence all alerts"),
	# Translators: a label for alerts reporting mode
	3: _("Custom")
}


# Zoom alerts rpeorting settings messages.
zoomAlertsToggleMessages: dict[str, str] = {
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"ParticipantHasJoined/LeftMeeting": _("participant has joined/left meeting"),
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"ParticipantHasJoined/LeftWaitingRoom": _("participant has joined/left waiting room"),
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"AudioMutedByHost": _("audio muted by host"),
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"VideoStoppedByHost": _("video stopped by host"),
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"ScreenSharingStarted/StoppedByParticipant": _("screen sharing started/stopped by participant"),
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"RecordingPermissionGranted/Revoked": _("recording permission granted/revoked"),
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"PublicIn-meetingChatReceived": _("public in-meeting chat received"),
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"PrivateIn-meetingChatReceived": _("private in-meeting chat received"),
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"In-meetingFileUploadCompleted": _("in-meeting file upload completed"),
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"HostPrivilegeGranted/Revoked": _("host privilege granted/revoked"),
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"ParticipantHasRaised/LoweredHand": _("participant has raised/lowered hand"),
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"RemoteControlPermissionGranted/Revoked": _("remote control permission granted/revoked"),
	# Translators: a message reported for the user when toggling reporting a spicific alert
	"IMChatReceived": _("IM chat received"),
}


# Translators: the label of the off state for reporting an alert
offLabel = _("off")


# Translators: the label of on state for reporting an alert
onLabel = _("on")


class AppModule(CoreAppModule):
	def __init__(self, processID, appName):
		super().__init__(processID, appName)
		eventHandler.requestEvents(
			"nameChange", processId=self.processID, windowClassName="zBubbleBaseClass")
		initConfiguration()
		categoryClasses = gui.settingsDialogs.NVDASettingsDialog.categoryClasses
		if ZoomEnhancementsSettingsPanel not in categoryClasses:
			categoryClasses.append(ZoomEnhancementsSettingsPanel)
		self.chatHistoryDialog = None
		self.chatHistoryList = []
		self.receivedChatPrefix = False
		self.chatPrefixText = ""

	def terminate(self):
		super().terminate()
		try:
			gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(ZoomEnhancementsSettingsPanel)
		except ValueError:
			pass

	def event_alert(self, obj, nextHandler):
		if regexs.publicInMeetingChatReceivedRegEx.fullmatch(obj.name) or regexs.privateInMeetingChatReceivedRegEx.fullmatch(obj.name):
			self._handleChatMessage(obj.name)
		match config.conf["zoomEnhancements"]["alertsReportingMode"]:
			case "Report all alerts":
				return nextHandler()
			case "Beep for alerts":
				tones.beep(1000, 50)
				return
			case "Silence all alerts":
				return
			case _:
				pass
		alert = obj.name
		if regexs.publicInMeetingChatReceivedRegEx.fullmatch(alert):
			if config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"]:
				nextHandler()
			return
		elif regexs.privateInMeetingChatReceivedRegEx.fullmatch(alert):
			if config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"]:
				nextHandler()
			return
		elif regexs.joinedLeftMeetingRegEx.fullmatch(alert):
			if config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"]:
				nextHandler()
			return
		elif regexs.joinedLeftWaitingRoomRegEx.fullmatch(alert):
			if config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"]:
				nextHandler()
			return
		elif regexs.audioMutedByHostRegEx.fullmatch(alert):
			if config.conf["zoomEnhancements"]["AudioMutedByHost"]:
				nextHandler()
			return
		elif regexs.videoStoppedByHostRegEx.fullmatch(alert):
			if config.conf["zoomEnhancements"]["VideoStoppedByHost"]:
				nextHandler()
			return
		elif regexs.screenSharingStartedStoppedByParticipantRegEx.fullmatch(alert):
			if config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"]:
				nextHandler()
			return
		elif regexs.recordingPermissionGrantedRevokedRegEx.fullmatch(alert):
			if config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"]:
				nextHandler()
			return
		elif regexs.inMeetingFileUploadCompletedRegEx.fullmatch(alert):
			if config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"]:
				nextHandler()
			return
		elif regexs.hostPrivilegeGrantedRevokedRegEx.fullmatch(alert):
			if config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"]:
				nextHandler()
			return
		elif regexs.raisedLoweredHandRegEx.fullmatch(alert):
			if config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"]:
				nextHandler()
			return
		elif regexs.iMChatReceivedRegEx.fullmatch(alert):
			if config.conf["zoomEnhancements"]["IMChatReceived"]:
				nextHandler()
			return
		else:
			nextHandler()

	def event_nameChange(self, obj, nextHandler):
		nextHandler()
		if obj.role == controlTypes.Role.STATICTEXT and obj.windowClassName == "zBubbleBaseClass":
			if self.receivedChatPrefix:
				obj.name = self.chatPrefixText + ": " + obj.name
				self.receivedChatPrefix = False
				self.chatPrefixText = ""
			elif regexs.inMeetingChatReceivedPrefixRegEx.fullmatch(obj.name):
				self.chatPrefixText = obj.name
				self.receivedChatPrefix = True
				return
			obj.role = controlTypes.Role.ALERT
			eventHandler.queueEvent("alert", obj)

	scriptCategory = SCRCAT_ZOOMENHANCEMENTS

	# Report custom alert reporting option changes.
	def zoomAlertsSettingsChange(self, setting: str):
		# Do nothing if alert reporting mode is not "custom".
		if config.conf["zoomEnhancements"]["alertsReportingMode"] != "Custom":
			return
		config.conf["zoomEnhancements"][setting] = not config.conf["zoomEnhancements"][setting]
		state = config.conf["zoomEnhancements"][setting]
		ui.message(
			# Translators: a message reported for the user when toggling reporting Zoom alerts
			_("Report {zoomAlert} {alertSetting}").format(
				zoomAlert=zoomAlertsToggleMessages[setting], alertSetting=onLabel if state else offLabel
			)
		)

	@script(
		description=_(
			# Translators: a description for a command to toggle reporting a spicific alert
			"Toggles reporting joined / left meeting alerts on / off"),
		gestures=[
			"kb:NVDA+control+1",
			"kb(desktop):NVDA+control+numpad1"
		]
	)
	def script_participantJoinedLeftMeeting(self, gesture):
		self.zoomAlertsSettingsChange("ParticipantHasJoined/LeftMeeting")

	@script(
		description=_(
			# Translators: a description for a command to toggle reporting a spicific alert
			"Toggles reporting joined / left Waiting Room alerts on / off"),
		gestures=[
			"kb:NVDA+control+2",
			"kb(desktop):NVDA+control+numpad2"
		]
	)
	def script_participantJoinedLeftWaitingRoom(self, gesture):
		self.zoomAlertsSettingsChange("ParticipantHasJoined/LeftWaitingRoom")

	@script(
		# Translators: a description for a command to toggle reporting a spicific alert
		description=_("Toggles reporting audio muted by host alerts on / off"),
		gestures=[
			"kb:NVDA+control+3",
			"kb(desktop):NVDA+control+numpad3"
		]
	)
	def script_audioMutedByHost(self, gesture):
		self.zoomAlertsSettingsChange("AudioMutedByHost")

	@script(
		description=_(
			# Translators: a description for a command to toggle reporting a spicific alert
			"Toggles reporting video stopped by host alerts on / off"),
		gestures=[
			"kb:NVDA+control+4",
			"kb(desktop):NVDA+control+numpad4"
		]
	)
	def script_videoStoppedByHost(self, gesture):
		self.zoomAlertsSettingsChange("VideoStoppedByHost")

	@script(
		description=_(
			# Translators: a description for a command to toggle reporting a spicific alert
			"Toggles reporting screen sharing started / stopped by participant alerts on / off"),
		gestures=[
			"kb:NVDA+control+5",
			"kb(desktop):NVDA+control+numpad5",
		]
	)
	def script_screenSharingStartedStopped(self, gesture):
		self.zoomAlertsSettingsChange("ScreenSharingStarted/StoppedByParticipant")

	@script(
		description=_(
			# Translators: a description for a command to toggle reporting a spicific alert
			"Toggles reporting recording permission granted / revoked alerts on / off"),
		gestures=[
			"kb:NVDA+control+6",
			"kb(desktop):NVDA+control+numpad6"
		]
	)
	def script_recordingPermissionGrantedRevoked(self, gesture):
		self.zoomAlertsSettingsChange("RecordingPermissionGranted/Revoked")

	@script(
		description=_(
			# Translators: a description for a command to toggle reporting a spicific alert
			"Toggles reporting public in-meeting chat received alerts on / off"),
		gestures=[
			"kb:NVDA+control+7",
			"kb(desktop):NVDA+control+numpad7"
		]
	)
	def script_publicInMeetingChatReceived(self, gesture):
		self.zoomAlertsSettingsChange("PublicIn-meetingChatReceived")

	@script(
		description=_(
			# Translators: a description for a command to toggle reporting a spicific alert
			"Toggles reporting private in-meeting chat received alerts on / off"),
		gestures=[
			"kb:NVDA+control+8",
			"kb(desktop):NVDA+control+numpad8"
		]
	)
	def script_privateInMeetingChatReceived(self, gesture):
		self.zoomAlertsSettingsChange("PrivateIn-meetingChatReceived")

	@script(
		description=_(
			# Translators: a description for a command to toggle reporting a spicific alert
			"Toggles reporting in-meeting file upload completed alerts on / off"),
		gestures=[
			"kb:NVDA+control+9",
			"kb(desktop):NVDA+control+numpad9"
		]
	)
	def script_inMeetingFileUploadCompleted(self, gesture):
		self.zoomAlertsSettingsChange("In-meetingFileUploadCompleted")

	@script(
		description=_(
			# Translators: a description for a command to toggle reporting a spicific alert
			"Toggles reporting host privilege granted / revoked alerts on / off"),
		gestures=[
			"kb:NVDA+control+0",
			"kb(desktop):NVDA+control+numpad0"
		]
	)
	def script_hostPrivilegeGrantedRevoked(self, gesture):
		self.zoomAlertsSettingsChange("HostPrivilegeGranted/Revoked")

	@script(
		description=_(
			# Translators: a description for a command to toggle reporting a spicific alert
			"Toggles reporting participant raised / lowered hand alerts on / off"),
		gestures=[
			"kb:NVDA+shift+control+1",
			"kb(desktop):NVDA+shift+control+numpad1"
		]
	)
	def script_participantRaisedLoweredHand(self, gesture):
		self.zoomAlertsSettingsChange("ParticipantHasRaised/LoweredHand")

	@script(
		description=_(
			# Translators: a description for a command to toggle reporting a spicific alert
			"Toggles reporting remote control permission granted /revoked alerts on / off"),
		gestures=[
			"kb:NVDA+shift+control+2",
			"kb(desktop):NVDA+shift+control+numpad2"
		]
	)
	def script_remoteControlPermissionGrantedRevoked(self, gesture):
		self.zoomAlertsSettingsChange("RemoteControlPermissionGranted/Revoked")

	@script(
		# Translators: a description for a command to toggle reporting a spicific alert
		description=_("Toggles reporting IM chat received alerts on / off"),
		gestures=[
			"kb:NVDA+shift+control+3",
			"kb(desktop):NVDA+shift+control+numpad3"
		]
	)
	def script_iMChatReceived(self, gesture):
		self.zoomAlertsSettingsChange("IMChatReceived")

	@script(
		# Translators: a description for a command to cycle between alerts reporting modes
		description=_("Toggles between reporting alerts as usual, beeping for the alert, silencing alerts completely, or custom mode where the user can choose which alerts are reported and which aren't."),
		gesture="kb:NVDA+Control+Shift+a"
	)
	def script_toggleAlertsMode(self, gesture):
		currentModeLabel = config.conf["zoomEnhancements"]["alertsReportingMode"]
		currentMode = 3
		for item in alertModeToLabel.items():
			if item[1] == currentModeLabel:
				currentMode = item[0]
		currentMode = (currentMode + 1) % 4
		config.conf["zoomEnhancements"]["alertsReportingMode"] = alertModeToLabel[currentMode]
		ui.message(alertModeToLabel[currentMode])

	def _handleChatMessage(self, alert):
		now = datetime.datetime.now()
		now = str(now.hour) + ":" + str(now.minute)
		alert += ", " + now
		self.chatHistoryList.append(alert)
		if self.chatHistoryDialog:
			self.chatHistoryDialog.itemList.InsertItems(
				[alert], self.chatHistoryDialog.itemList.GetCount())

	@script(
		# Translators: a description for a command to show the add-on settings dialog
		description=_("Shows Zoom enhancements settings dialog"),
		gesture="kb:NVDA+z"
	)
	def script_showSettingsDialog(self, gesture):
		gui.mainFrame.popupSettingsDialog(NVDASettingsDialog, ZoomEnhancementsSettingsPanel)

	@script(
		# Translators: a description for a command to show chat history dialog
		description=_("Shows chat history dialog"),
		gesture="kb:NVDA+control+h"
	)
	def script_showChatHistoryDialog(self, gesture):
		gui.mainFrame.prePopup()
		self.chatHistoryDialog = ChatHistoryDialog(
			# Translaters: the title of the chat history dialog
			_("Chat history"), self.chatHistoryList)
		self.chatHistoryDialog.Show()
		gui.mainFrame.postPopup()
