from HeroBasicTypes import json_timeplace
from EventProcessor import EventProcessor

@EventProcessor(104)
def SCommandManagerTargetPointEvent_processor(player, event):
    player.SCommandManagerTargetPointEvents.append(
        json_timeplace(event, 'm_target')
    )

@EventProcessor(49)
def SCameraUpdateEvent_processor(player, event):
    player.SCameraUpdateEvents.append(
        json_timeplace(event, 'm_target')
    )
