# dialogs.py
# A part of zoomEnhancements add-on
# This file is covered by the GNU General Public License
# See the file COPYING for more details

import gui
from gui import guiHelper
from gui.nvdaControls import DPIScaledDialog, CustomCheckListBox
import wx
import config
import addonHandler
import webbrowser
from . import regexs


addonHandler.initTranslation()


def findLinks(text: str) -> list[str]:
	"""Returns the links in a chat message, in order and without duplicates."""
	links = []
	for match in regexs.linkRegEx.finditer(text):
		link = match.group(0).rstrip(".,;:!?)]}")
		if link not in links:
			links.append(link)
	return links


class ZoomEnhancementsSettingsPanel(gui.settingsDialogs.SettingsPanel):
	# Translators: Title for the settings dialog
	title = _("Zoom Enhancements")
	# Translators: description for the settings dialog
	panelDescription = _("Configures Zoom Enhancements add-on settings for the Zoom web conference tool.")

	def makeSettings(self, settingsSizer: wx.BoxSizer):
		settingsSizerHelper = guiHelper.BoxSizerHelper(
			self, sizer=settingsSizer)
		from . import alertModeToLabel
		modeChoices = [item[1] for item in alertModeToLabel.items()]
		self.alertsReportingMode = settingsSizerHelper.addLabeledControl(
			# Translators: the label of the combo box in the settings dialog
			_("&Alerts reporting mode:"), wx.Choice, choices=modeChoices)
		currentModeLabel = config.conf["zoomEnhancements"]["alertsReportingMode"]
		currentMode = 0
		for item in alertModeToLabel.items():
			if (item[1] == currentModeLabel):
				currentMode = item[0]
		self.alertsReportingMode.SetSelection(currentMode)

		alertsReportingOptions = (
			# Translators: a label of a checkbox in the settings dialog
			_("participant has joined/left meeting"),
			# Translators: a label of a checkbox in the settings dialog
			_("participant has joined/left waiting room"),
			# Translators: a label of a checkbox in the settings dialog
			_("audio muted by host"),
			# Translators: a label of a checkbox in the settings dialog
			_("video stopped by host"),
			# Translators: a label of a checkbox in the settings dialog
			_("screen sharing started/stopped by a participant"),
			# Translators: a label of a checkbox in the settings dialog
			_("recording permission granted/revoked"),
			# Translators: a label of a checkbox in the settings dialog
			_("public in-meeting chat received"),
			# Translators: a label of a checkbox in the settings dialog
			_("private in-meeting chat received"),
			# Translators: a label of a checkbox in the settings dialog
			_("in-meeting file upload completed"),
			# Translators: a label of a checkbox in the settings dialog
			_("host privilege granted/revoked"),
			# Translators: a label of a checkbox in the settings dialog
			_("participant has raised/lowered hand (host only)"),
			# Translators: a label of a checkbox in the settings dialog
			_("remote control permission granted/revoked"),
			# Translators: a label of a checkbox in the settings dialog
			_("IM chat received"),
		)
		alertsReportingValues = (
			config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"],
			config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"],
			config.conf["zoomEnhancements"]["AudioMutedByHost"],
			config.conf["zoomEnhancements"]["VideoStoppedByHost"],
			config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"],
			config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"],
			config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"],
			config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"],
			config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"],
			config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"],
			config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"],
			config.conf["zoomEnhancements"]["RemoteControlPermissionGranted/Revoked"],
			config.conf["zoomEnhancements"]["IMChatReceived"],
		)
		alertsReportingCheckableListLabel = _(
			# Translators: the label of the checkable list in the settings dialog
			"&Choose which alerts should be reported (effective only when custom mode is selected):"
		)
		self.alertsReportingCheckableList = settingsSizerHelper.addLabeledControl(
			alertsReportingCheckableListLabel, CustomCheckListBox, choices=alertsReportingOptions
		)
		for pos, setting in enumerate(alertsReportingValues):
			self.alertsReportingCheckableList.Check(
				pos, check=setting
			)
		self.alertsReportingCheckableList.SetSelection(0)

	def onSave(self):
		from . import alertModeToLabel
		newMode = [x[1] for x in alertModeToLabel.items()][
			self.alertsReportingMode.GetSelection()
		]
		config.conf["zoomEnhancements"]["alertsReportingMode"] = newMode
		# Alerts reporting checkable list
		config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftMeeting"] = self.alertsReportingCheckableList.IsChecked(0)
		config.conf["zoomEnhancements"]["ParticipantHasJoined/LeftWaitingRoom"] = self.alertsReportingCheckableList.IsChecked(1)
		config.conf["zoomEnhancements"]["AudioMutedByHost"] = self.alertsReportingCheckableList.IsChecked(2)
		config.conf["zoomEnhancements"]["VideoStoppedByHost"] = self.alertsReportingCheckableList.IsChecked(3)
		config.conf["zoomEnhancements"]["ScreenSharingStarted/StoppedByParticipant"] = self.alertsReportingCheckableList.IsChecked(4)
		config.conf["zoomEnhancements"]["RecordingPermissionGranted/Revoked"] = self.alertsReportingCheckableList.IsChecked(5)
		config.conf["zoomEnhancements"]["PublicIn-meetingChatReceived"] = self.alertsReportingCheckableList.IsChecked(6)
		config.conf["zoomEnhancements"]["PrivateIn-meetingChatReceived"] = self.alertsReportingCheckableList.IsChecked(7)
		config.conf["zoomEnhancements"]["In-meetingFileUploadCompleted"] = self.alertsReportingCheckableList.IsChecked(8)
		config.conf["zoomEnhancements"]["HostPrivilegeGranted/Revoked"] = self.alertsReportingCheckableList.IsChecked(9)
		config.conf["zoomEnhancements"]["ParticipantHasRaised/LoweredHand"] = self.alertsReportingCheckableList.IsChecked(10)
		config.conf["zoomEnhancements"]["RemoteControlPermissionGranted/Revoked"] = self.alertsReportingCheckableList.IsChecked(11)
		config.conf["zoomEnhancements"]["IMChatReceived"] = self.alertsReportingCheckableList.IsChecked(12)


class ChatHistoryDialog(DPIScaledDialog):

	def __init__(self, title: str, items: list[str]):
		windowStyle = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.MAXIMIZE_BOX
		super().__init__(gui.mainFrame, title=title, style=windowStyle)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = guiHelper.BoxSizerHelper(self, wx.VERTICAL)
		self.itemList = wx.ListBox(self)
		if items:
			self.itemList.InsertItems(items, 0)
		self.itemList.Bind(wx.EVT_LISTBOX, self.onSelectionChange)
		sHelper.addItem(self.itemList)
		# One button per link in the selected message.
		self.linkButtonsSizer = wx.BoxSizer(wx.VERTICAL)
		self.linkButtons = []
		sHelper.addItem(self.linkButtonsSizer, flag=wx.EXPAND)
		sHelper.addDialogDismissButtons(wx.CLOSE, True)
		mainSizer.Add(sHelper.sizer, border=guiHelper.BORDER_FOR_DIALOGS,
					  flag=wx.ALL | wx.EXPAND, proportion=1)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.SetMinSize(self.scaleSize(self.MIN_SIZE))
		self.SetSize(self.scaleSize(self.INITIAL_SIZE))
		self.CentreOnScreen()

	def onSelectionChange(self, evt):
		self.updateLinkButtons()

	def updateLinkButtons(self):
		for button in self.linkButtons:
			button.Destroy()
		self.linkButtons = []
		self.linkButtonsSizer.Clear()
		selection = self.itemList.GetSelection()
		# Keep link buttons right after the message list in tab order, before Close.
		previous = self.itemList
		if selection != wx.NOT_FOUND:
			for link in findLinks(self.itemList.GetString(selection)):
				# The button label is the link itself.
				# Escape ampersands so wx does not treat them as access keys.
				button = wx.Button(self, label=link.replace("&", "&&"))
				button.Bind(wx.EVT_BUTTON, lambda evt, link=link: self.openLink(link))
				self.linkButtonsSizer.Add(button, flag=wx.EXPAND | wx.TOP, border=guiHelper.SPACE_BETWEEN_BUTTONS_VERTICAL)
				button.MoveAfterInTabOrder(previous)
				previous = button
				self.linkButtons.append(button)
		self.Layout()

	def openLink(self, link: str):
		if link.lower().startswith("www."):
			link = "https://" + link
		webbrowser.open(link)
		self.Close()

	INITIAL_SIZE = (800, 480)
	MIN_SIZE = (470, 240)
