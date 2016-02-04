import HeroAnalysis
import HeroAnalysisExporter
from collections import defaultdict

import sqlite3
import os

cwd = os.getcwd()
replay_path = r'{}\replays\ben\zag2.StormReplay'.format(cwd)

analysis = HeroAnalysis.analyze(replay_path)
ben = HeroAnalysis.get_player_by_name(analysis.players, 'TheBenD')

connection = sqlite3.connect(r'{}\database\database.db'.format(cwd))
cursor = connection.cursor()
records = []
for e in ben.SCmdEvents:
    a = e.ability
    link = None if not a else a.link
    cmd_index = None if not a else a.cmd_index
    
    tp = e.target_point
    x, y, z = None, None, None
    if tp: x, y, z = tp.x, tp.y, tp.z
    
    records.append((
        1,
        e.loop,
        link, cmd_index,
        e.cmd_flags,
        e.other_unit,
        e.sequence,
        x, y, z,
        e.player_id,
        e.target_unit_flags,
        e.snapshot_unit_link,
        e.tag
    ))

for r in records:
    print r

blanks = ','.join('?'*14)
insert_qry = 'INSERT INTO cmd_event VALUES ({})'.format(blanks)
cursor.executemany(insert_qry, records)

connection.commit()
connection.close()
'''
# abilities = set(str(e.ability) for e in ben.SCmdEvents)
abilities = defaultdict(int)
for event in ben.SCmdEvents:
    print event
    ability = event.ability
    abilities[str(ability)] += 1
    
# print sorted(abilities)
for k in sorted(abilities.iterkeys()):
    print '{:7} {:3}'.format(k, abilities[k])

#for e in ben.SCmdEvents:
#    abilities.add(e.ability)
#    print e
# print HeroAnalysisExporter.analysis_string(analysis)
'''