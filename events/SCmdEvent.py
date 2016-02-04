from HeroBasicTypes import Point
from EventProcessor import EventProcessor
from collections import namedtuple

Ability = namedtuple('Ability', 'link cmd_index')
Ability.__repr__ = lambda self: 'L{0.link}-I{0.cmd_index}'.format(self)

class SCmdEvent:
    def __repr__(self):
        target = None
        if self.player_id is not None:
            target = 'P{0.player_id} U{0.snapshot_unit_link} T{0.tag}'.format(self)
        return '{:60} | {:20}'.format(
            '@{0.loop:5} {0.ability:8} [{0.cmd_flags:7}] @ {0.target_point}: {0.other_unit}'.format(self),
            target
        )

@EventProcessor(27)
def SCmdEvent_processor(player, event):
    ce = SCmdEvent()
    ce.target_point = None
    ce.player_id = None
    ce.target_unit_flags = None
    ce.snapshot_unit_link = None
    ce.tag = None
    ce.ability = None
    
    ce.loop = event['_gameloop']
    ce.cmd_flags = event['m_cmdFlags']
    ce.other_unit = event['m_otherUnit']
    ce.sequence = event['m_sequence'] # almost all unique
    
    ability = event['m_abil']
    if ability:
        ce.ability = Ability(
            link = ability['m_abilLink'],
            cmd_index = ability['m_abilCmdIndex']
        )

    # always a single-item dict
    k, v = next(event['m_data'].iteritems())
    if k == 'TargetPoint':
        ce.target_point = Point(v)
    elif k == 'TargetUnit':
        ce.target_point = Point(v['m_snapshotPoint'])
        ce.player_id = v['m_snapshotControlPlayerId'] # == m_snapshotUpkeepPlayerId
        # ce.timer = v['m_timer'] # always 0
        ce.target_unit_flags = v['m_targetUnitFlags'] # almost always 111 
        ce.snapshot_unit_link = v['m_snapshotUnitLink']
        ce.tag = v['m_tag']

    player.SCmdEvents.append(ce)
