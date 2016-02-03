from EventProcessor import EventProcessor

class SUnitClickEvent:
    def __repr__(self):
        return '{:>6} {}'.format(
            '@{}'.format(self.loop),
            self.unit_tag
        )

@EventProcessor(39)
def SUnitClickEvent_processor(player, event):
    uc = SUnitClickEvent()
    uc.loop = event['_gameloop']
    uc.unit_tag = event['m_unitTag']
    player.SUnitClickEvents.append(uc)
