import HeroParser
from Player import Player
from HeroBasicTypes import *
from collections import defaultdict

from events import *
from events.EventProcessor import get_event_processor, event_ids

SUnitDiedEvent_id = 2

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
        
        p.win = (d['m_result'] == 1) # 1 = WIN, 2 = LOSS
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

class HeroAnalysis:
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
            if pid != s['m_workingSetSlotId']:
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
        # Use decorator for tracker handlers just like event handlers
        self.deaths = [SUnitDiedEvent.get(t) for t in trackers if t['_eventid'] == SUnitDiedEvent_id]

        game_events = parser.get_game_events()
        self.event_counts = defaultdict(int)
        for event in game_events:
            event_id = event['_eventid']
            uid = event['_userid']['m_userId']
            
            # only a few that are beyond regular uids
            if uid > len(self.player_slots):
                continue
                print event
                print dir(event)

            player = self.player_slots[uid]
            get_event_processor(event_id)(player, event)

            # count to know which to parse later
            self.event_counts[event_id] += 1

    def __repr__(self):
        team1 = [p for p in self.players.itervalues() if p.team == 0]
        team2 = [p for p in self.players.itervalues() if p.team == 1]

        return \
'''Replay Path: {}
Version: {}
Duration in Loops: {}
Map: {}
Time: {}
Mini-Save: {}
Max Users: {}
Single Player: {}
Blizzard Map: {}
Competitive: {}
Practice: {}
Ranked: {}
Lock Teams: {}
m_amm: {}

Team 1 ({}):
{}

Team 2 ({}):
{}

Deaths: {}

Event Counts:
{}'''.format(
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
            # '\n'.join(str(d) for d in self.deaths),
            len(self.deaths),
            '\n'.join(
                '{:3} ({:40}): {}'.format(k, event_ids[k], v)
                for k, v in self.event_counts.iteritems()
            )
        )

