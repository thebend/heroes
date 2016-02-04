from events import EventProcessor
from trackers import TrackerProcessor

def lf(data):
    return '\n'.join(str(i) for i in data)

def analysis_string(analysis):
    team1 = [p for p in analysis.players.itervalues() if p.team == 0]
    team2 = [p for p in analysis.players.itervalues() if p.team == 1]

    return \
'''Replay Path: {0.replay}
Version: {0.version}
Duration in Loops: {0.duration_loops}
Map: {0.map}
Time: {0.time}
Mini-Save: {0.mini_save}
Max Users: {0.max_users}
Single Player: {0.single_player}
Blizzard Map: {0.blizzard_map}
Competitive: {0.competitive}
Practice: {0.practice}
Ranked: {0.ranked}
Lock Teams: {0.lock_teams}
m_amm: {0.m_amm}

Team 1 ({1}):
{2}

Team 2 ({3}):
{4}

Deaths: {5}

Event Counts:
{6}

Tracker Counts:
{7}'''.format(
        analysis,
        'Win' if team1[0].win else 'Loss',
        lf(team1),
        'Win' if team2[0].win else 'Loss',
        lf(team2),
        # '\n'.join(str(d) for d in a.deaths),
        len(analysis.deaths),
        lf(
            '{:3} {:35} {:>5}'.format(k, EventProcessor.event_ids[k], v)
            for k, v in analysis.event_counts.iteritems()
        ),
        lf(
            '{:3} {:3} {:31} {:5}'.format(
                k,
                TrackerProcessor.tracker_ids[k][0],
                TrackerProcessor.tracker_ids[k][1],
                v
            ) for k, v in analysis.tracker_counts.iteritems()
        )
    )
