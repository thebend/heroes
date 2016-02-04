from EventProcessor import EventProcessor
from collections import namedtuple

SCommandManagerStateEvent = namedtuple(
    'SCommandManagerStateEvent',
    'loop state sequence'
)
SCommandManagerStateEvent.__repr__ = lambda self: \
    '{0:>6} {1.state} {1.sequence:4}'.format(
        '@{}'.format(self.loop), self
    )

@EventProcessor(103)
def SCommandManagerStateEvent_processor(player, event):
    player.SCommandManagerStateEvents.append(SCommandManagerStateEvent(
        loop = event['_gameloop'],
        state = event['m_state'],
        sequence = event['m_sequence']
    ))