from EventProcessor import EventProcessor
from collections import namedtuple

SUserOptionsEvent = namedtuple(
    'SUserOptionsEvent',
    'fully_downloaded camera_follow mac_version'
)

@EventProcessor(7)
def SUserOptionsEvent_processor(player, event):
    player.user_options = SUserOptionsEvent(
        fully_downloaded = event['m_gameFullyDownloaded'],
        camera_follow = event['m_cameraFollow'],
        mac_version = event['m_platformMac']
    )