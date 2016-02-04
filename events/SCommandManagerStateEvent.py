from EventProcessor import EventProcessor

class SCommandManagerStateEvent:
    def __repr__(self):
        return '{0:>6} {1.state} {1.sequence:4}'.format(
            '@{}'.format(self.loop), self
        )

@EventProcessor(103)
def SCommandManagerStateEvent_processor(player, event):
    cms = SCommandManagerStateEvent()
    cms.loop = event['_gameloop']
    cms.state = event['m_state']
    cms.sequence = event['m_sequence']
    player.SCommandManagerStateEvents.append(cms)