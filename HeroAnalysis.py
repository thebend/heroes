import HeroParser
from Player import Player
from HeroBasicTypes import Color
from collections import defaultdict

from events import *
from trackers import *

def get_player(d):
    p = Player()
    p.team = d['m_teamId']
    p.observe = d['m_observe']
    p.control = d['m_control']
    p.race = d['m_race'] # ' ', meaningless - there is no race
    p.handicap = d['m_handicap'] # always 100, no handicaps
    p.win = (d['m_result'] == 1) # 1 = WIN, 2 = LOSS
    p.slot = d['m_workingSetSlotId'] # Game slots 0-9
    p.hero = d['m_hero']
    p.name = d['m_name']
    
    c = d['m_color']
    p.color = Color(c['m_r'], c['m_g'], c['m_b'], c['m_a']) # either red or blue
    
    t = d['m_toon']
    p.id = t['m_id']
    p.region = t['m_region']
    p.realm = t['m_realm']
    return p

def get_player_by_name(players, name):
    for p in players:
        if p.name == name:
            return p
    raise LookupError('Could not find player named "{}"'.format(name))

class HeroAnalysis:
    def __init__(self, replay):
        self.replay = replay
        self.players = {}
        self.player_slots = {}
        self.deaths = []

def get_player_scopes(scopes):
    player_scopes = defaultdict(dict)
    for player, settings in scopes.iteritems():
        for k, v in settings.iteritems():
            player_scopes[player][k] = v[0]['value']
    return player_scopes

def analyze(replay):
    a = HeroAnalysis(replay)
    parser = HeroParser.HeroParser(replay)
    a.parser = parser

    # this doesn't seem to do anything useful
    # attributes = parser.get_attributes()
    # scopes = get_player_scopes(attributes['scopes'])
    
    ph = parser.get_protocol_header()
    a.version = ph['m_version']['m_build']
    a.duration_loops = ph['m_elapsedGameLoops']

    pd = parser.get_protocol_details()
    a.map = pd['m_title']
    a.mini_save = pd['m_miniSave']
    a.time = pd['m_timeUTC'] # what format is this?  Huge int

    for data in pd['m_playerList']:
        p = get_player(data)
        a.players[p.id] = p
        a.player_slots[p.slot] = p

    pid = parser.get_protocol_init_data()
    sls = pid['m_syncLobbyState']
    # for uid in sls['m_userInitialData'] # not relevant

    ls = sls['m_lobbyState']
    a.max_users = ls['m_maxUsers']
    a.single_player = ls['m_isSinglePlayer']
    a.game_duration = ls['m_gameDuration']

    for s in ls['m_slots']:
        # Look up active player
        pid = s['m_userId']
        if pid is None: continue
        # Just making sure assumption is correct across replays
        if pid != s['m_workingSetSlotId']:
            raise ValueError('UserID and WorkingSetSlotID should match')
        p = a.player_slots[pid]

        p.mount = s['m_mount']
        p.skin = s['m_skin']
        p.hero2 = s['m_hero']

    gd = sls['m_gameDescription']
    a.extension_mod = gd['m_hasExtensionMod']
    a.blizzard_map = gd['m_isBlizzardMap']

    go = gd['m_gameOptions']
    # Are competitive/practice/ranked mutually exclusive?
    a.competitive = go['m_competitive']
    a.practice = go['m_practice']
    a.ranked = go['m_ranked']
    a.lock_teams = go['m_lockTeams'] # ???
    a.m_amm = go['m_amm'] # ???

    # why are these called trackers?  WHich events do I need to care about?
    trackers = parser.get_trackers()
    a.tracker_counts = defaultdict(int)
    for tracker in trackers:
        event_id = tracker['_eventid']
        a.tracker_counts[event_id] += 1
        TrackerProcessor.get(event_id)(a, tracker)

    game_events = parser.get_game_events()
    a.event_counts = defaultdict(int)
    for event in game_events:
        event_id = event['_eventid']
        uid = event['_userid']['m_userId']
        
        # only a few that are beyond regular uids
        # should look into this again?
        if uid > len(a.player_slots):
            continue
            print event
            print dir(event)

        player = a.player_slots[uid]
        EventProcessor.get(event_id)(player, event)

        # count to know which to parse later
        a.event_counts[event_id] += 1

    return a