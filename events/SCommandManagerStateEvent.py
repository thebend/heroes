class SCommandManagerStateEvent:
    def __init__(self, event):
        self.loop = event['_gameloop']
        self.state = event['m_state']
        self.sequence = event['m_sequence']

    def __repr__(self):
        return '{:>6} {} {:4}'.format(
            '@{}'.format(self.loop),
            self.state,
            self.sequence
        )