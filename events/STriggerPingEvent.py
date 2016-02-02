from HeroBasicTypes import TimePlace

class STriggerPingEvent():
    def __init__(self, event):
        self.timeplace = TimePlace.from_json(event, 'm_point')
        self.minimap = event['m_pingedMinimap']
        self.option = event['m_option']
        self.unit = event['m_unit']

    def __repr__(self):
        return '{} {} {:2} U{}'.format(
            self.timeplace,
            'Minimap' if self.minimap else 'Gamemap',
            self.option,
            self.unit
        )