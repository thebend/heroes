from events import EventProcessor
from trackers import TrackerProcessor

def analysis_string(a):
    team1 = [p for p in a.players.itervalues() if p.team == 0]
    team2 = [p for p in a.players.itervalues() if p.team == 1]

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
{}

Tracker Counts:
{}'''.format(
        a.replay,
        a.version,
        a.duration_loops,
        a.map,
        a.time,
        a.mini_save,
        a.max_users,
        a.single_player,
        a.blizzard_map,
        a.competitive,
        a.practice,
        a.ranked,
        a.lock_teams,
        a.m_amm,
        'Win' if team1[0].win else 'Loss',
        '\n'.join(str(p) for p in team1),
        'Win' if team2[0].win else 'Loss',
        '\n'.join(str(p) for p in team2),
        # '\n'.join(str(d) for d in a.deaths),
        len(a.deaths),
        '\n'.join(
            '{:3} {:35} {:>5}'.format(k, EventProcessor.event_ids[k], v)
            for k, v in a.event_counts.iteritems()
        ),
        '\n'.join(
            '{:3} {:3} {:31} {:5}'.format(
                k,
                TrackerProcessor.tracker_ids[k][0],
                TrackerProcessor.tracker_ids[k][1],
                v
            ) for k, v in a.tracker_counts.iteritems()
        )
    )
