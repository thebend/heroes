# Return a function that does nothing by default
def default_processor(player, event):
    pass

processors = {}
def get(id):
    try: return processors[id]
    except KeyError: return default_processor

def EventProcessor(id):
    def set_processor(processor):
        processors[id] = processor
        return processor
    return set_processor

# These do vary slightly between protocol versions
# eg. 110 is SHeroTalentTreeSelectedEvent and HeroTalentSelectedEvent
event_ids = {
    5: 'SUserFinishedLoadingSyncEvent', # unused
    7: 'SUserOptionsEvent', # patched/camera follow/mac
    9: 'SBankFileEvent', # unused
    10: 'SBankSectionEvent', # unused
    11: 'SBankKeyEvent', # unused
    12: 'SBankValueEvent', # unused
    13: 'SBankSignatureEvent', # unused
    14: 'SCameraSaveEvent', # unused
    21: 'SSaveGameEvent', # unused
    22: 'SSaveGameDoneEvent', # unused
    23: 'SLoadGameDoneEvent', # unused
    25: 'SCommandManagerResetEvent',
    26: 'SGameCheatEvent', # unused
    27: 'SCmdEvent',
    28: 'SSelectionDeltaEvent', # unused
    29: 'SControlGroupUpdateEvent', # unused
    30: 'SSelectionSyncCheckEvent', # unused
    31: 'SResourceTradeEvent', # unused
    32: 'STriggerChatMessageEvent',
    33: 'SAICommunicateEvent', # unused
    34: 'SSetAbsoluteGameSpeedEvent', # unused
    35: 'SAddAbsoluteGameSpeedEvent', # unused
    36: 'STriggerPingEvent',
    37: 'SBroadcastCheatEvent', # unused
    38: 'SAllianceEvent', # unused
    39: 'SUnitClickEvent',
    40: 'SUnitHighlightEvent', # unused
    41: 'STriggerReplySelectedEvent', # unused
    43: 'SHijackReplayGameEvent', # unused
    44: 'STriggerSkippedEvent', # unused
    45: 'STriggerSoundLengthQueryEvent', # unused
    46: 'STriggerSoundOffsetEvent', # loop/sound
    47: 'STriggerTransmissionOffsetEvent',
    48: 'STriggerTransmissionCompleteEvent',
    49: 'SCameraUpdateEvent',
    50: 'STriggerAbortMissionEvent', # unused
    51: 'STriggerPurchaseMadeEvent', # unused
    52: 'STriggerPurchaseExitEvent', # unused
    53: 'STriggerPlanetMissionLaunchedEvent', # unused
    54: 'STriggerPlanetPanelCanceledEvent', # unused
    55: 'STriggerDialogControlEvent',
    56: 'STriggerSoundLengthSyncEvent', # unused
    57: 'STriggerConversationSkippedEvent', # unused
    58: 'STriggerMouseClickedEvent', # unused
    59: 'STriggerMouseMovedEvent', # unused
    60: 'SAchievementAwardedEvent', # unused
    62: 'STriggerTargetModeUpdateEvent', # unused
    63: 'STriggerPlanetPanelReplayEvent', # unused
    64: 'STriggerSoundtrackDoneEvent',
    65: 'STriggerPlanetMissionSelectedEvent', # unused
    66: 'STriggerKeyPressedEvent',
    67: 'STriggerMovieFunctionEvent', # unused
    68: 'STriggerPlanetPanelBirthCompleteEvent', # unused
    69: 'STriggerPlanetPanelDeathCompleteEvent', # unused
    70: 'SResourceRequestEvent', # unused
    71: 'SResourceRequestFulfillEvent', # unused
    72: 'SResourceRequestCancelEvent', # unused
    73: 'STriggerResearchPanelExitEvent', # unused
    74: 'STriggerResearchPanelPurchaseEvent', # unused
    75: 'STriggerResearchPanelSelectionChangedEvent', # unused
    77: 'STriggerMercenaryPanelExitEvent', # unused
    78: 'STriggerMercenaryPanelPurchaseEvent', # unused
    79: 'STriggerMercenaryPanelSelectionChangedEvent', # unused
    80: 'STriggerVictoryPanelExitEvent', # unused
    81: 'STriggerBattleReportPanelExitEvent', # unused
    82: 'STriggerBattleReportPanelPlayMissionEvent', # unused
    83: 'STriggerBattleReportPanelPlaySceneEvent', # unused
    84: 'STriggerBattleReportPanelSelectionChangedEvent', # unused
    85: 'STriggerVictoryPanelPlayMissionAgainEvent', # unused
    86: 'STriggerMovieStartedEvent', # unused
    87: 'STriggerMovieFinishedEvent', # unused
    88: 'SDecrementGameTimeRemainingEvent', # unused
    89: 'STriggerPortraitLoadedEvent', # unused
    90: 'STriggerCustomDialogDismissedEvent', # unused
    91: 'STriggerGameMenuItemSelectedEvent', # unused
    93: 'STriggerPurchasePanelSelectedPurchaseItemChangedEvent', # unused
    94: 'STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent', # unused
    95: 'STriggerButtonPressedEvent', # unused
    96: 'STriggerGameCreditsFinishedEvent', # unused
    97: 'STriggerCutsceneBookmarkFiredEvent', # unused
    98: 'STriggerCutsceneEndSceneFiredEvent',
    99: 'STriggerCutsceneConversationLineEvent', # unused
    100: 'STriggerCutsceneConversationLineMissingEvent', # unused
    101: 'SGameUserLeaveEvent',
    102: 'SGameUserJoinEvent',
    103: 'SCommandManagerStateEvent',
    104: 'SCommandManagerTargetPointEvent',
    105: 'SCommandManagerTargetUnitEvent',
    106: 'STriggerAnimLengthQueryByNameEvent', # unused
    107: 'STriggerAnimLengthQueryByPropsEvent', # unused
    108: 'STriggerAnimOffsetEvent', # unused
    109: 'SCatalogModifyEvent', # unused
    110: 'SHeroTalentSelectedEvent'
}
