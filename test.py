import HeroParser

replay_path = r'C:\heroes\replays\ben\zag1.StormReplay'

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

class Player():
	def __repr__(self):
		return \
'''Team {}/{} | {} / {} ({})
Color: {}
Result: {}
'''.format(
	self.team,
	self.workingSetSlotId,
	self.hero,
	self.name,
	self.id,
	self.color,
	self.result
)

class HeroReplay():
	@staticmethod
	def get_players(player_data):
		players = []
		for d in player_data:
			p = Player()
			# print d
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
			p.result = d['m_result'] # win/loss?
			p.workingSetSlotId = d['m_workingSetSlotId'] # ???
			p.hero = d['m_hero']
			p.name = d['m_name']

			players.append(p)
		return players

	def __init__(self, replay_path):
		self.replay_path = replay_path
		parser = HeroParser.HeroParser(replay_path)
		self.parser = parser

		ph = parser.get_protocol_header()
		self.version = ph['m_version']['m_build']
		self.duration_loops = ph['m_elapsedGameLoops']

		pd = parser.get_protocol_details()
		self.map = pd['m_title']

		# Not sure what format this is in?
		# 7 digits too large for epoch seconds
		self.time = pd['m_timeUTC']

		self.players = HeroReplay.get_players(pd['m_playerList'])
		self.mini_save = pd['m_miniSave']

		pid = parser.get_protocol_init_data()
		sls = pid['m_syncLobbyState']

		# Must look up data per hero and save with hero
		for uid in sls['m_userInitialData']:
			self.mount = uid['m_mount']
			self.observe = uid['m_observe']
			self.team_preference = uid['m_teamPreference']['m_team']
			self.custom_interface = uid['m_customInterface']
			self.highest_league = uid['m_highestLeague']
			self.clan_tag = uid['m_clanTag']
			self.clan_logo = uid['m_clanLogo']
			self.combined_race_levels = uid['m_combinedRaceLevels']
			self.race_prefreence = uid['m_racePreference']['m_race']
			self.skin = uid['m_skin']
			self.hero = uid['m_hero']
			self.name = uid['m_name']

		ls = sls['m_lobbyState']
		self.max_users = ls['m_maxUsers']

		# Must look up data per hero and save with hero
		for s in ls['m_slots']:
			# Look up correct player
			print s['m_mount']
			print s['m_teamId']
			print s['m_userId']
			print s['m_workingSetSlotId']
			print s['m_skin']
			print s['m_hero']
		self.single_player = ls['m_isSinglePlayer']
		self.game_duration = ls['m_gameDuration']

		gd = sls['m_gameDescription']
		self.extension_mod = gd['m_hasExtensionMod']
		self.blizzard_map = gd['m_isBlizzardMap']

		go = gd['m_gameOptions']
		self.competitive = go['m_competitive']
		self.practice = go['m_practice']
		self.ranked = go['m_ranked']
		self.lock_teams = go['m_lockTeams'] # ???
		self.m_amm = go['m_amm'] # ???

	def __repr__(self):
		return \
'''Replay Path: {}
Version: {}
Duration in Loops: {}
Map: {}
Time: {}
Mini-Save: {}

Players:
{}'''.format(
		self.replay_path,
		self.version,
		self.duration_loops,
		self.map,
		self.time,
		self.mini_save,
		'========\n'.join(str(p) for p in self.players)
)

h = HeroReplay(replay_path)
# print h
