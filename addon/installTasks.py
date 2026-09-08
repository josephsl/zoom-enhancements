# zoom-enhancements/installTasks.py
# Copyright 2026 Joseph Lee, released under GPL.

# Registers add-on config spec/settings blueprint.

import config
confspecRegistrationAvailable = hasattr(config, "configSections")

def onInstall() -> None:
	# Register this add-on's settings with NVDA's configuration system.
	# If running NVDA 2026.3, register the confspec here, otherwise do it from the app module.
	if not confspecRegistrationAvailable:
		return
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
	config.configSections.registerSection("zoomEnhancements", confspec)
