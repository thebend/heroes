from HeroBasicTypes import Point
from EventProcessor import EventProcessor

class SCommandManagerTargetUnitEvent:
    def __repr__(self):
        return '{:>6} {:2} {} {:3} {:3} {:8}'.format(
            '@{}'.format(self.loop),
            self.player_id,
            self.point,
            self.target_unit_flags,
            self.snapshot_unit_link,
            self.tag
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
