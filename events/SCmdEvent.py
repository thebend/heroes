from HeroBasicTypes import Point
from EventProcessor import EventProcessor

class Ability:
    def __init__(self, abil):
        self.link = abil['m_abilLink']
        self.cmd_index = abil['m_abilCmdIndex']

    def __repr__(self):
        return 'L{}-I{}'.format(
            self.link,
            self.cmd_index
        )

class SCmdEvent:
    def __repr__(self):
        return '{:60} | {:20}'.format(
            '@{:5} {:8} [{:7}] @ {}: {}'.format(
                self.loop,
                self.ability,
                self.cmd_flags,
                self.target_point,
                self.other_unit
            ), 'P{} U{} T{}'.format(
                self.player_id,
                self.snapshot_unit_link,
                self.tag
            )
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

    try:
        ce.ability = Ability(event['m_abil'])
    except TypeError:
        ce.ability = None
    
    ce.cmd_flags = event['m_cmdFlags']
    
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
