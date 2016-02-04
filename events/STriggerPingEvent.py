from HeroBasicTypes import json_timeplace
from EventProcessor import EventProcessor
from collections import namedtuple

STriggerPingEvent = namedtuple('STriggerPingEvent', 'timeplace minimap option unit')
STriggerPingEvent.__repr__ = lambda self: '{0.timeplace} {1} {0.option:2} U{0.unit}'.format(
    self, 'Minimap' if self.minimap else 'Gamemap'
)

@EventProcessor(36)
def STriggerPingEvent_processor(player, event):
    player.pings.append(STriggerPingEvent(
        timeplace = json_timeplace(event, 'm_point'),
        minimap = event['m_pingedMinimap'],
        option = event['m_option'],
        unit = event['m_unit']
    ))