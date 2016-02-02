from HeroBasicTypes import Point

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
    def __init__(self, event):
        # set defaults
        self.target_point = None
        self.player_id = None
        self.target_unit_flags = None
        self.snapshot_unit_link = None
        self.tag = None
        
        self.loop = event['_gameloop']

        try:
            self.ability = Ability(event['m_abil'])
        except TypeError:
            self.ability = None
        
        self.cmd_flags = event['m_cmdFlags']
        
        # always a single-item dict
        k, v = event['m_data'].items()[0]
        if k == 'TargetPoint':
            self.target_point = Point(v['x'], v['y'], v['z'])

        elif k == 'TargetUnit':
            p = v['m_snapshotPoint']
            self.target_point = Point(p['x'], p['y'], p['z'])

            # same as m_snapshotUpkeepPlayerId
            self.player_id = v['m_snapshotControlPlayerId']

            # always 0
            # self.timer = v['m_timer']

            # almost always 111 
            self.target_unit_flags = v['m_targetUnitFlags']

            self.snapshot_unit_link = v['m_snapshotUnitLink']

            self.tag = v['m_tag']

        self.other_unit = event['m_otherUnit']
        
        # almost all unique
        self.sequence = event['m_sequence']

    def compact_display(self):
        l1 = '''@{:5} {:8} [{}] @ {}: {}'''.format(
            self.loop,
            self.ability,
            self.cmd_flags,
            self.target_point,
            self.other_unit
        )
        l2 = '''P{} U{} T{}'''.format(
            self.player_id,
            self.snapshot_unit_link,
            self.tag
        )
        return '{:55} | {:20}'.format(l1, l2)

    def __repr__(self):
        return self.compact_display()
