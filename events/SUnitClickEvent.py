class SUnitClickEvent:
    def __init__(self, event):
        self.loop = event['_gameloop']
        self.unit_tag = event['m_unitTag']

    def __repr__(self):
        return '{:>6} {}'.format(
            '@{}'.format(self.loop),
            self.unit_tag
        )