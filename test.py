import HeroAnalysis
import HeroAnalysisExporter
from collections import defaultdict

import sqlite3
import os

cwd = os.getcwd()
replay_path = r'{}\replays\ben\butcher-test.StormReplay'.format(cwd)

analysis = HeroAnalysis.analyze(replay_path)
ben = HeroAnalysis.get_player_by_name(analysis.players, 'TheBenD')

print HeroAnalysisExporter.analysis_string(analysis)

for e in ben.SCmdEvents:
    print e
for e in ben.SCommandManagerStateEvents:
    print e
    
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

# set up database
cursor.execute('DROP TABLE IF EXISTS cmd_event');
event_table_qry = open('database/SCmdEvent.sql','r').read()
cursor.execute(event_table_qry)

blanks = ','.join('?'*14)
insert_qry = 'INSERT INTO cmd_event VALUES ({})'.format(blanks)
cursor.executemany(insert_qry, records)

connection.commit()
connection.close()
