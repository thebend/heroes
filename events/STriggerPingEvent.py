from HeroBasicTypes import json_timeplace
from EventProcessor import EventProcessor

class STriggerPingEvent():
    def __repr__(self):
        maptype = 'Minimap' if self.minimap else 'Gamemap'
        return '{0.timeplace} {1} {0.option:2} U{0.unit}'.format(self, maptype)

@EventProcessor(36)
def STriggerPingEvent_processor(player, event):
    p = STriggerPingEvent()
    p.timeplace = json_timeplace(event, 'm_point')
    p.minimap = event['m_pingedMinimap']
    p.option = event['m_option']
    p.unit = event['m_unit']
    player.pings.append(p)