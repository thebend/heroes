from EventProcessor import EventProcessor
from collections import namedtuple

SUnitClickEvent = namedtuple('SUnitClickEvent', 'loop unit_tag')
SUnitClickEvent.__repr__ = lambda self: '{:>6} {}'.format(
    '@{}'.format(self.loop),
    self.unit_tag
)

@EventProcessor(39)
def SUnitClickEvent_processor(player, event):
    player.SUnitClickEvents.append(SUnitClickEvent(
        loop = event['_gameloop'],
        unit_tag = event['m_unitTag']
    ))
