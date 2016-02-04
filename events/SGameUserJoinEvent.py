from EventProcessor import EventProcessor
from collections import namedtuple

SGameUserJoinEvent = namedtuple('SGameUserJoinEvent', 'loop handle')

@EventProcessor(102)
def SGameUserJoinEvent_processor(player, event):
    player.joins.append(SGameUserJoinEvent(
        loop = event['_gameloop'],
        handle = event['m_toonHandle']
    ))