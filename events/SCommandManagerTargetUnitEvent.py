from HeroBasicTypes import Point

class SCommandManagerTargetUnitEvent:
    def __init__(self, event):
        self.loop = event['_gameloop']
        t = event['m_target']
        self.player_id = t['m_snapshotControlPlayerId']
        self.point = Point(t['m_snapshotPoint'])
        self.target_unit_flags = t['m_targetUnitFlags']
        self.tag = t['m_tag']
        self.snapshot_unit_link = t['m_snapshotUnitLink']

    def __repr__(self):
        return '{:>6} {:2} {} {:3} {:3} {:8}'.format(
            '@{}'.format(self.loop),
            self.player_id,
            self.point,
            self.target_unit_flags,
            self.snapshot_unit_link,
            self.tag
        )