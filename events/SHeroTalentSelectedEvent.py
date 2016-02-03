from EventProcessor import EventProcessor

class SHeroTalentSelectedEvent:
    def __repr__(self):
        return '@{} {}'.format(self.loop, self.index)

@EventProcessor(110)
def SHeryoTalentSelectedEvent_processor(player, event):
    hts = SHeroTalentSelectedEvent()
    hts.loop = event['_gameloop']
    hts.index = event['m_index']
    player.SHeroTalentSelectedEvents.append(hts)
