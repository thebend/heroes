from HeroBasicTypes import Point
from EventProcessor import EventProcessor

class Ability:
    def __init__(self, abil):
        self.link = abil['m_abilLink']
        self.cmd_index = abil['m_abilCmdIndex']

    def __repr__(self):
        return 'L{0.link}-I{0.cmd_index}'.format(self)

class SCmdEvent:
    def __repr__(self):
        return '{:60} | {:20}'.format(
            '@{0.loop:5} {0.ability:8} [{0.cmd_flags:7}] @ {0.target_point}: {0.other_unit}'.format(self),
            'P{0.player_id} U{0.snapshot_unit_link} T{0.tag}'.format(self)
        )

@EventProcessor(27)
def SCmdEvent_processor(player, event):
    ce = SCmdEvent()
    ce.target_point = None
    ce.player_id = None
    ce.target_unit_flags = None
    ce.snapshot_unit_link = None
    ce.tag = None
    
    ce.loop = event['_gameloop']
    ce.cmd_flags = event['m_cmdFlags']
    
    try: ce.ability = Ability(event['m_abil'])
    except TypeError: ce.ability = None
    
    # always a single-item dict
    k, v = event['m_data'].items()[0]
    if k == 'TargetPoint':
        ce.target_point = Point(v)
    elif k == 'TargetUnit':
        ce.target_point = Point(v['m_snapshotPoint'])
        ce.player_id = v['m_snapshotControlPlayerId'] # == m_snapshotUpkeepPlayerId
        # ce.timer = v['m_timer'] # always 0
        ce.target_unit_flags = v['m_targetUnitFlags'] # almost always 111 
        ce.snapshot_unit_link = v['m_snapshotUnitLink']
        ce.tag = v['m_tag']

    ce.other_unit = event['m_otherUnit']
    ce.sequence = event['m_sequence'] # almost all unique
    
    player.SCmdEvents.append(ce)
