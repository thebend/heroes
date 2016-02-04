from HeroBasicTypes import Point
from EventProcessor import EventProcessor
from collections import namedtuple

SCommandManagerTargetUnitEvent = namedtuple(
    'SCommandManagerTargetUnitEvent',
    'loop player_id point target_unit_flags tag snapshot_unit_link'
)
SCommandManagerTargetUnitEvent.__repr__ = lambda self: \
    '{0:>6} {1.player_id:2} {1.point} {1.target_unit_flags:3} {1.snapshot_unit_link:3} {1.tag:8}'.format(
        '@{}'.format(self.loop), self
    )

@EventProcessor(105)
def SCommandManagerTargetUnitEvent_processor(player, event):
    t = event['m_target']
    player.SCommandManagerTargetUnitEvents.append(SCommandManagerTargetUnitEvent(
        loop = event['_gameloop'],
        player_id = t['m_snapshotControlPlayerId'],
        point = Point(t['m_snapshotPoint']),
        target_unit_flags = t['m_targetUnitFlags'],
        tag = t['m_tag'],
        snapshot_unit_link = t['m_snapshotUnitLink']
    ))
