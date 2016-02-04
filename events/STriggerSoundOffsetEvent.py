from EventProcessor import EventProcessor
from collections import namedtuple

STriggerSoundOffsetEvent = namedtuple(
    'STriggerSoundOffsetEvent', 'loop sound'
)

@EventProcessor(46)
def STriggerSoundOffsetEvent_processor(player, event):
    player.STriggerSoundOffsetEvents.append(STriggerSoundOffsetEvent(
        loop = event['_gameloop'],
        sound = event['m_sound']
    ))