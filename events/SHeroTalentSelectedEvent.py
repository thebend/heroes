class SHeroTalentSelectedEvent:
    def __init__(self, event):
        self.loop = event['_gameloop']
        self.index = event['m_index']

    def __repr__(self):
        return '@{} {}'.format(self.loop, self.index)
