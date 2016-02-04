from EventProcessor import EventProcessor
from collections import namedtuple

Chat = namedtuple('Chat', 'loop message')
Chat.__repr__ = lambda self: '{:6}: {}'.format(
    '@{}'.format(self.loop),
    self.message
)

@EventProcessor(32)
def STriggerChatMessageEvent_processor(player, event):
    player.chats.append(Chat(
        loop = event['_gameloop'],
        message = event['m_chatMessage']
    ))
