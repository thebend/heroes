import HeroParser
from collections import defaultdict

SUnitDiedEvent_id = 2
SCmdEvent_id = 27
STriggerChatMessageEvent_id = 32
STriggerPingEvent_id = 36
SUnitClickEvent_id = 39
SCameraUpdateEvent_id = 49
SCommandManagerStateEvent_id = 103
SCommandManagerTargetPointEvent_id = 104
SCommandManagerTargetUnitEvent_id = 105
SHeroTalentSelectedEvent_id = 110

# These do vary slightly between protocol versions
# eg. 110 is SHeroTalentTreeSelectedEvent
# and 110 is HeroTalentSelectedEvent
game_event_ids = {
	5: 'SUserFinishedLoadingSyncEvent',
	7: 'SUserOptionsEvent',
	9: 'SBankFileEvent',
	10: 'SBankSectionEvent',
	11: 'SBankKeyEvent',
	12: 'SBankValueEvent',
	13: 'SBankSignatureEvent',
	14: 'SCameraSaveEvent',
	21: 'SSaveGameEvent',
	22: 'SSaveGameDoneEvent',
	23: 'SLoadGameDoneEvent',
	25: 'SCommandManagerResetEvent',
	26: 'SGameCheatEvent',
	27: 'SCmdEvent',
	28: 'SSelectionDeltaEvent',
	29: 'SControlGroupUpdateEvent',
	30: 'SSelectionSyncCheckEvent',
	31: 'SResourceTradeEvent',
	32: 'STriggerChatMessageEvent',
	33: 'SAICommunicateEvent',
	34: 'SSetAbsoluteGameSpeedEvent',
	35: 'SAddAbsoluteGameSpeedEvent',
	36: 'STriggerPingEvent',
	37: 'SBroadcastCheatEvent',
	38: 'SAllianceEvent',
	39: 'SUnitClickEvent',
	40: 'SUnitHighlightEvent',
	41: 'STriggerReplySelectedEvent',
	43: 'SHijackReplayGameEvent',
	44: 'STriggerSkippedEvent',
	45: 'STriggerSoundLengthQueryEvent',
	46: 'STriggerSoundOffsetEvent',
	47: 'STriggerTransmissionOffsetEvent',
	48: 'STriggerTransmissionCompleteEvent',
	49: 'SCameraUpdateEvent',
	50: 'STriggerAbortMissionEvent',
	51: 'STriggerPurchaseMadeEvent',
	52: 'STriggerPurchaseExitEvent',
	53: 'STriggerPlanetMissionLaunchedEvent',
	54: 'STriggerPlanetPanelCanceledEvent',
	55: 'STriggerDialogControlEvent',
	56: 'STriggerSoundLengthSyncEvent',
	57: 'STriggerConversationSkippedEvent',
	58: 'STriggerMouseClickedEvent',
	59: 'STriggerMouseMovedEvent',
	60: 'SAchievementAwardedEvent',
	62: 'STriggerTargetModeUpdateEvent',
	63: 'STriggerPlanetPanelReplayEvent',
	64: 'STriggerSoundtrackDoneEvent',
	65: 'STriggerPlanetMissionSelectedEvent',
	66: 'STriggerKeyPressedEvent',
	67: 'STriggerMovieFunctionEvent',
	68: 'STriggerPlanetPanelBirthCompleteEvent',
	69: 'STriggerPlanetPanelDeathCompleteEvent',
	70: 'SResourceRequestEvent',
	71: 'SResourceRequestFulfillEvent',
	72: 'SResourceRequestCancelEvent',
	73: 'STriggerResearchPanelExitEvent',
	74: 'STriggerResearchPanelPurchaseEvent',
	75: 'STriggerResearchPanelSelectionChangedEvent',
	77: 'STriggerMercenaryPanelExitEvent',
	78: 'STriggerMercenaryPanelPurchaseEvent',
	79: 'STriggerMercenaryPanelSelectionChangedEvent',
	80: 'STriggerVictoryPanelExitEvent',
	81: 'STriggerBattleReportPanelExitEvent',
	82: 'STriggerBattleReportPanelPlayMissionEvent',
	83: 'STriggerBattleReportPanelPlaySceneEvent',
	84: 'STriggerBattleReportPanelSelectionChangedEvent',
	85: 'STriggerVictoryPanelPlayMissionAgainEvent',
	86: 'STriggerMovieStartedEvent',
	87: 'STriggerMovieFinishedEvent',
	88: 'SDecrementGameTimeRemainingEvent',
	89: 'STriggerPortraitLoadedEvent',
	90: 'STriggerCustomDialogDismissedEvent',
	91: 'STriggerGameMenuItemSelectedEvent',
	93: 'STriggerPurchasePanelSelectedPurchaseItemChangedEvent',
	94: 'STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent',
	95: 'STriggerButtonPressedEvent',
	96: 'STriggerGameCreditsFinishedEvent',
	97: 'STriggerCutsceneBookmarkFiredEvent',
	98: 'STriggerCutsceneEndSceneFiredEvent',
	99: 'STriggerCutsceneConversationLineEvent',
	100: 'STriggerCutsceneConversationLineMissingEvent',
	101: 'SGameUserLeaveEvent',
	102: 'SGameUserJoinEvent',
	103: 'SCommandManagerStateEvent',
	104: 'SCommandManagerTargetPointEvent',
	105: 'SCommandManagerTargetUnitEvent',
	106: 'STriggerAnimLengthQueryByNameEvent',
	107: 'STriggerAnimLengthQueryByPropsEvent',
	108: 'STriggerAnimOffsetEvent',
	109: 'SCatalogModifyEvent',
	110: 'SHeroTalentSelectedEvent'
}

class Death():
	def __repr__(self):
		return '{:6} ({:3}, {:3}) - {} > {}'.format(
			'@{}'.format(self.game_loop),
			self.point[0],
			self.point[1],
			self.killerUnitTagIndex,
			self.unitTagIndex
		)

class Ping():
	def __repr__(self):
		return '{:6} {}: ({:6}, {:6})'.format(
			'@{}'.format(self.game_loop),
			self.userid,
			self.point[0],
			self.point[1]
		)

class Chat():
	def __repr__(self):
		return '{:6} {}: {}'.format(
			'@{}'.format(self.game_loop),
			self.userid,
			self.string
		)

class Color():
	def __init__(self, r, g, b, a):
		self.r = r
		self.g = g
		self.b = b
		self.a = a

	def __repr__(self):
		return '({},{},{},{})'.format(
			self.r,
			self.g,
			self.b,
			self.a
		)

class SCmdEvent():
	def __init__(self, event):
		self.gameloop = event['_gameloop']
		self.abil = event['m_abil']
		self.cmd_flags = event['m_cmdFlags']
		self.data = event['m_data']
		try:
			tp = self.data['TargetPoint']
			self.target_point = (tp['x'], tp['y'], tp['z'])
		except:
			self.target_point = (None, None, None)
		self.other_unit = event['m_otherUnit']
		self.sequence = event['m_sequence']
		self.unit_group = event['m_unitGroup']

	def __repr__(self):
		return \
'''@{} -> {} ({}) @ ({},{},{}): {}, {}, {}'''.format(
	self.gameloop,
	self.abil,
	self.cmd_flags,
	self.target_point[0],
	self.target_point[1],
	self.target_point[2],
	self.other_unit,
	self.sequence,
	self.unit_group
)

class Player():
	def __init__(self):
		self.SCmdEvents = []

	def SCmdEvents_append(self, event):
		self.SCmdEvents.append(SCmdEvent(event))

	def __repr__(self):
		return \
'''{} - {:10} ({:8}) | {}.{}.{} on {}
SCmdEvents:
{}'''.format(
	self.slot,
	self.name,
	self.id,
	self.hero,
	self.hero2,
	self.skin,
	self.mount,
	'\n'.join(str(e) for e in self.SCmdEvents)
)

def get_players(player_data):
	players = {}
	for d in player_data:
		p = Player()
		c = d['m_color']
		# Is there any relevance to red vs blue team?
		# These colors aren't customizable, just red or blue
		p.color = Color(c['m_r'], c['m_g'], c['m_b'], c['m_a'])
		p.team = d['m_teamId']
		p.observe = d['m_observe']
		p.control = d['m_control']
		p.race = d['m_race'] # ' ', meaningless - there is no race
		p.handicap = d['m_handicap'] # always 100, no handicaps
		t = d['m_toon']
		p.id = t['m_id']
		p.region = t['m_region']
		p.realm = t['m_realm']
		p.result = d['m_result'] # 1 = WIN, 2 = LOSS?
		p.win = (p.result == 1)
		p.slot = d['m_workingSetSlotId'] # Game slots 0-9
		p.hero = d['m_hero']
		p.name = d['m_name']
		players[p.id] = p

	player_slots = [None] * len(players)
	for p in players.itervalues():
		player_slots[p.slot] = p

	return players, player_slots

def get_player_by_name(players, name):
	for p in players:
		if p.name == name:
			return p
	raise LookupError('Could not find player named "{}"'.format(name))

class HeroAnalysis():
	def __init__(self, replay=None):
		self.replay = replay

	def set_protocol(self, protocol):
		raise NotImplementedError('Protocol is detected automatically')

	def set_replay(self, replay):
		self.replay = replay

	def analyze(self):
		parser = HeroParser.HeroParser(self.replay)
		self.parser = parser

		ph = parser.get_protocol_header()
		self.version = ph['m_version']['m_build']
		self.duration_loops = ph['m_elapsedGameLoops']

		pd = parser.get_protocol_details()
		self.map = pd['m_title']

		# Not sure what format this is in?
		# 7 digits too large for epoch seconds
		self.time = pd['m_timeUTC']

		self.players, self.player_slots = get_players(pd['m_playerList'])
		self.mini_save = pd['m_miniSave']

		pid = parser.get_protocol_init_data()
		sls = pid['m_syncLobbyState']

		# Must look up data per hero and save with hero
		# None of this data is useful at all!
		"""
		for uid in sls['m_userInitialData']:
			self.p1 = Player()
			self.p1.mount = uid['m_mount']
			self.p1.observe = uid['m_observe']
			self.p1.team_preference = uid['m_teamPreference']['m_team']
			self.p1.custom_interface = uid['m_customInterface']
			self.p1.highest_league = uid['m_highestLeague']
			self.p1.clan_tag = uid['m_clanTag']
			self.p1.clan_logo = uid['m_clanLogo']
			self.p1.combined_race_levels = uid['m_combinedRaceLevels']
			self.p1.race_preference = uid['m_racePreference']['m_race']
			self.p1.skin = uid['m_skin']
			self.p1.hero = uid['m_hero']
			self.p1.name = uid['m_name']
		"""

		ls = sls['m_lobbyState']
		self.max_users = ls['m_maxUsers']

		# Must look up data per hero and save with hero
		for s in ls['m_slots']:
			# Look up correct player
			pid = s['m_userId']
			if pid is None: continue
			# Shouldn't need this line
			# Just making sure assumption is correct across replays
			if pid <> s['m_workingSetSlotId']:
				raise Exception('UserID and WorkingSetSlotID should match')
			p = self.player_slots[pid]

			p.mount = s['m_mount']
			p.skin = s['m_skin']
			p.hero2 = s['m_hero']

		self.single_player = ls['m_isSinglePlayer']
		self.game_duration = ls['m_gameDuration']

		gd = sls['m_gameDescription']
		self.extension_mod = gd['m_hasExtensionMod']
		self.blizzard_map = gd['m_isBlizzardMap']

		go = gd['m_gameOptions']
		# Are competitive/practice/ranked mutually exclusive?
		self.competitive = go['m_competitive']
		self.practice = go['m_practice']
		self.ranked = go['m_ranked']
		self.lock_teams = go['m_lockTeams'] # ???
		self.m_amm = go['m_amm'] # ???

		self.pings = []
		self.chats = []
		messages = parser.get_messages()
		for m in messages:
			event = m['_event']
			if event == 'NNet.Game.SPingMessage':
				p = Ping()
				p.game_loop = m['_gameloop']
				p.userid = m['_userid']['m_userId']
				p.recipient = m['m_recipient'] # Always 1
				point = m['m_point']
				p.point = (point['x'], point['y'])
				self.pings.append(p)

			if event == 'NNet.Game.SChatMessage':
				c = Chat()
				c.game_loop = m['_gameloop']
				c.userid = m['_userid']['m_userId']
				c.recipient = m['m_recipient'] # Always 1
				c.string = m['m_string']
				self.chats.append(c)

		trackers = parser.get_trackers()
		"""
tracker_event_types = {
    0: (183, 'NNet.Replay.Tracker.SPlayerStatsEvent'),
    1: (184, 'NNet.Replay.Tracker.SUnitBornEvent'),
    2: (185, 'NNet.Replay.Tracker.SUnitDiedEvent'),
    3: (186, 'NNet.Replay.Tracker.SUnitOwnerChangeEvent'),
    4: (187, 'NNet.Replay.Tracker.SUnitTypeChangeEvent'),
    5: (188, 'NNet.Replay.Tracker.SUpgradeEvent'),
    6: (184, 'NNet.Replay.Tracker.SUnitInitEvent'),
    7: (189, 'NNet.Replay.Tracker.SUnitDoneEvent'),
    8: (191, 'NNet.Replay.Tracker.SUnitPositionsEvent'),
    9: (192, 'NNet.Replay.Tracker.SPlayerSetupEvent'),
}
		"""
		self.deaths = []
		for t in trackers:
			if t['_eventid'] == SUnitDiedEvent_id:
				d = Death()
				d.game_loop = t['_gameloop']
				d.killer_player_id = t['m_killerPlayerId']
				d.killerUnitTagIndex = t['m_killerUnitTagIndex']
				d.unitTagIndex = t['m_unitTagIndex']
				d.point = (t['m_x'], t['m_y'])
				self.deaths.append(d)

		game_events = parser.get_game_events()
		self.event_counts = defaultdict(int)
		# self.player_events = defaultdict(list)
		for ge in game_events:
			eid = ge['_eventid']
			uid = ge['_userid']['m_userId']
			if uid > len(self.player_slots):
				continue
				print ge
				print dir(ge)
			p = self.player_slots[uid]
			if eid == SCmdEvent_id:
				p.SCmdEvents_append(ge)

			# self.player_events[uid]
			self.event_counts[eid] += 1
			# SCmdEvent (27) - 4466
			# STriggerChatMessageEvent (32) - 2
			# STriggerPingEvent (36) - 16
			# SUnitClickEvent (39) - 764
			# SCameraUpdateEvent (49) - 9996

			# SCommandManagerStateEvent (103) - 33425
			# SCommandManagerTargetPointEvent (104) - 30734
			# SCommandManagerTargetUnitEvent (105) - 1606

			# SHeroTalentSelectedEvent (110) - 64

	def __repr__(self):
		team1 = [p for p in self.players.itervalues() if p.team == 0]
		team2 = [p for p in self.players.itervalues() if p.team == 1]

		return open('AnalysisTemplate.txt','r').read().format(
			self.replay,
			self.version,
			self.duration_loops,
			self.map,
			self.time,
			self.mini_save,
			self.max_users,
			self.single_player,
			self.blizzard_map,
			self.competitive,
			self.practice,
			self.ranked,
			self.lock_teams,
			self.m_amm,
			'Win' if team1[0].win else 'Loss',
			'\n'.join(str(p) for p in team1),
			'Win' if team2[0].win else 'Loss',
			'\n'.join(str(p) for p in team2),
			'\n'.join(str(c) for c in self.chats),
			'\n'.join(str(p) for p in self.pings),
			# '\n'.join(str(d) for d in self.deaths),
			'Omitted',
			'\n'.join(
				'{:3} ({:40}): {}'.format(k, game_event_ids[k], v)
				for k, v in self.event_counts.iteritems()
			)
		)

