from HeroBasicTypes import json_timeplace
from EventProcessor import EventProcessor

class STriggerPingEvent():
    def __repr__(self):
        return '{} {} {:2} U{}'.format(
            self.timeplace,
            'Minimap' if self.minimap else 'Gamemap',
            self.option,
            self.unit
        )

@EventProcessor(36)
def STriggerPingEvent_processor(player, event):
    p = STriggerPingEvent()
    p.timeplace = json_timeplace(event, 'm_point')
    p.minimap = event['m_pingedMinimap']
    p.option = event['m_option']
    p.unit = event['m_unit']
    player.STriggerPingEvents.append(p)