from EventProcessor import EventProcessor
from collections import namedtuple

SHeroTalentSelectedEvent = namedtuple('SHeroTalentSelectedEvent', 'loop index')
SHeroTalentSelectedEvent.__repr__ = lambda self: '@{0.loop} {0.index}'.format(self)

@EventProcessor(110)
def SHeroTalentSelectedEvent_processor(player, event):
    player.SHeroTalentSelectedEvents.append(SHeroTalentSelectedEvent(
        loop = event['_gameloop'],
        index = event['m_index']
    ))
