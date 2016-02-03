from EventProcessor import EventProcessor

class Chat:
    def __repr__(self):
        return '{:6}: {}'.format(
            '@{}'.format(self.loop),
            self.message
        )

@EventProcessor(32)
def STriggerChatMessageEvent_processor(player, event):
    c = Chat()
    c.loop = event['_gameloop']
    c.message = event['m_chatMessage']
    player.chats.append(c)
