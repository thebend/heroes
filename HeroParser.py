import mpyq
from heroprotocol import protocol29406

class HeroParser():
	def __init__(self, replay_path):
		self.replay_path = replay_path
		self.archive = mpyq.MPQArchive(replay_path)

		# Read the protocol header, this can be read with any protocol
		self.contents = self.archive.header['user_data_header']['content']
		# header = heroprotocol.protocol29406.decode_replay_header(contents)
		self.header = protocol29406.decode_replay_header(self.contents)
		# The header's baseBuild determines which protocol to use
		self.baseBuild = self.header['m_version']['m_baseBuild']

		module = 'heroprotocol.protocol%s' % self.baseBuild
		try:
			self.protocol = __import__(module, fromlist=['heroprotocol'])
		except ImportError as e:
			raise TypeError('Unsupported base build: %d' % baseBuild)

	def get_protocol_header(self):
		"""
		Returns a dictionary:
		m_useScaledTime = false
		m_version
			m_baseBuild = 36144
			m_minor = 12
			m_revision = 0
			m_flags = 1
			m_major = 0
			m_build = 36359
		m_type = 2
		m_signature = 'Heroes of the Storm replay\x1b11'
		m_ngdpRootKey = {}
		m_elapsedGameLoops = 19556
		m_dataBuildNum = 36359
		"""
		return self.header

	def get_protocol_details(self):
		"""
		Returns a dictionary:
		m_imageFilePath = ''
		m_description = ''
		m_timeLocalOffset = -252000000000L
		m_thumbnail
			m_file = 'ReplaysPreviewImage.tga'
		m_defaultDifficulty = 7
		m_restartAsTransitionMap = False
		m_title = 'Tomb of the Spider Queen'
		m_campaignIndex = 0
		m_modPaths = None
		m_cacheHandles = list of hex values
		m_timeUTC = 130812119943125997L
		m_isBlizzardMap = True
		m_mapFileName = ''
		m_gameSpeed = 4
		m_playerList = complex dict
		m_miniSave = False
		m_difficulty = ''
		"""
		contents = self.archive.read_file('replay.details')
		return self.protocol.decode_replay_details(contents)

	def get_protocol_init_data(self):
		"""
		Returns dict of 3 complicated dicts
		m_syncLobbyState
			m_userInitialData = list
				m_testAuto = False
				m_mount = ''
				m_observe = 0
				m_teamPreference
					m_team = None
				m_toonHandle = ''
				m_customInterface = False
				m_highestLeague = 0
				m_clanTag = ''
				m_testMap = False
				m_clanLogo = None
				m_examine = False
				m_testType = 0
				m_combinedRaceLevels = 0
				m_randomSeed = 0
				m_racePreference
					m_race = None
				m_skin = ''
				m_hero = ''
				m_name = 'BIOCiiDE'
			m_lobbyState
				m_maxUsers = 10
				m_slots = list
					m_mount = 'HorseAlmond'
					m_rewards = list of longs
					m_handicap = 100
					m_aiBuild = 0
					m_teamId = 0
					m_observe = 0
					m_control = 2
					m_tandemLeaderUserId = None
					m_commanderLevel = 0
					m_toonHandle = '1-Hero-1-1715249'
					m_logoIndex = 0
					m_artifacts = list of empty strings
					m_commander = ''
					m_racePref
						m_race = None
					m_colorPref
						m_color = 3
					m_licenses = empty list
					m_userId = 0
					m_workingSetSlodId = 0
					m_skin = ''
					m_hero = 'Muradin'
					m_difficulty = 7
				m_defaultDifficulty = 7
				m_isSinglePlayer = False
				m_phase = 0
				m_hostUserId = None
				m_maxObservers = 6
				m_defaultAIBuild = 0
				m_pickedMapTag = 0
				m_randomSeed = 458461899
				m_gameDuration = 0
			m_gameDescription
				m_maxRaces = 3
				m_maxTeams = 10
				m_hasExtensionMod = False
				m_maxColors = 16
				m_isBlizzardMap = True
				m_gameOptions
					m_competitive = True
					m_practice = False
					m_ranked = True
					m_lockTeams = True
					m_amm = True
					m_battleNet = True
					m_fog = 0
					m_noVictoryOrDefeat = False
					m_heroDuplicatesAllowed = True
					m_advanceSharedControl = False
					m_cooperative = False
					m_clientDebugFlags = 33
					m_observers = 0
					m_teamsTogether = False
					m_randomRaces = False
					m_userDifficulty = 0
					m_defaultDifficulty = 7
					m_isCoopMode = False
					m_mapFileName = ''
					m_defaultAIBuild = 0
					m_gameType = 0
					m_randomValue = 458461899
					m_maxObservers = 6
					m_maxUsers = 10
					m_modFileSyncChecksum = 3487869853L
					m_mapSizeX = 248
					m_maxPlayers = 10
					m_cacheHandles = list of hex codes
					m_gamespeed = 4
					m_maxControls = 1
					m_gameCacheName = 'Dflt'
					m_mapAuthorName = '1-Hero-1-26'
					m_isPremadeFFA = False
					m_mapSizeY = 216
					m_mapFileSyncChecksum = 408550135L
					m_slotDescriptions = list
						m_allowedRaces = (3, 4)
						m_allowedColors = (16, 1024)
						m_allowedAIBUilds = (96, 0)
						m_allowedDifficulty = (32, 3456106496L)
						m_allowedObserveTypes = (3, 7)
						m_allowedControls = (255, huge long number)
		"""
		contents = self.archive.read_file('replay.initData')
		return self.protocol.decode_replay_initdata(contents)

	def get_game_events(self):
		"""
		Returns a list of dictionaries containing most game data
		"""
		contents = self.archive.read_file('replay.game.events')
		return self.protocol.decode_replay_game_events(contents)

	def get_messages(self):
		"""
		Returns generator of dicts
		_eventid = 2
		_event = 'NNet.Game.SLoadingProgressMessage'
		_bits = 56
		m_progress = 28L
		_gameloop = 0
		_userid
			m_userid = 4

		m_recipient = 1
		_eventid = 1
		_event = 'NNet.Game.SpingMessage'
		_gameloop = 8556
		_bits = 96
		_userid
			m_userid = 9
		m_point
			y = 469480L
			x = 494367L
		"""
		contents = self.archive.read_file('replay.message.events')
		return self.protocol.decode_replay_message_events(contents)

	def get_trackers(self):
		"""
		Returns list of dicts
		m_unitTagIndex = 64
		m_unitTagRecycle = 1
		_eventid = 1
		m_controlPlayerId = 0
		_event = 'NNet.Replay.Tracker.SUnitBornEvent'
		_gameLoop = 0
		m_y = 53
		m_x = 140
		_bits = 384
		m_upkeepPlayerId = 12
		m_unitTypeName = 'TownWallRadial17L2'
		"""
		contents = self.archive.read_file('replay.tracker.events')
		return self.protocol.decode_replay_tracker_events(contents)

	def get_attributes(self):
		"""
		Returns source, mapNamespace, scopes
		source is 0
		mapNamespace is 999
		scopes is a complicated dictionary
		"""
		contents = self.archive.read_file('replay.attributes.events')
		return self.protocol.decode_replay_attributes_events(contents)

