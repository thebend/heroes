from EventProcessor import EventProcessor
from collections import namedtuple

SGameUserLeaveEvent = namedtuple('SGameUserLeaveEvent', 'loop reason')

@EventProcessor(101)
def SGameUserLeaveEvent_processor(player, event):
    player.drops.append(SGameUserLeaveEvent(
        loop = event['_gameloop'],
        reason = event['m_leaveReason']
    ))