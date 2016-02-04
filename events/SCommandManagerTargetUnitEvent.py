from HeroBasicTypes import Point
from EventProcessor import EventProcessor

class SCommandManagerTargetUnitEvent:
    def __repr__(self):
        return '{0:>6} {1.player_id:2} {1.point} {1.target_unit_flags:3} {1.snapshot_unit_link:3} {1.tag:8}'.format(
            '@{}'.format(self.loop), self
        )

@EventProcessor(105)
def SCommandManagerTargetUnitEvent_processor(player, event):
    cmtu = SCommandManagerTargetUnitEvent()
    cmtu.loop = event['_gameloop']
    t = event['m_target']
    cmtu.player_id = t['m_snapshotControlPlayerId']
    cmtu.point = Point(t['m_snapshotPoint'])
    cmtu.target_unit_flags = t['m_targetUnitFlags']
    cmtu.tag = t['m_tag']
    cmtu.snapshot_unit_link = t['m_snapshotUnitLink']
    player.SCommandManagerTargetUnitEvents.append(cmtu)
