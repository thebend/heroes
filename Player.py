def lf(data):
    return '\n'.join(str(i) for i in data)

class Player:
    def __init__(self):
        self.SCmdEvents = []
        self.SHeroTalentSelectedEvents = []
        self.SCommandManagerStateEvents = []
        self.SCommandManagerTargetPointEvents = []
        self.SCommandManagerTargetUnitEvents = []
        self.SUnitClickEvents = []
        self.SCameraUpdateEvents = []
        self.chats = []
        self.pings = []

    def __repr__(self):
        return \
'''{0.slot} - {0.name:10} ({0.id:8}) | {0.hero}.{0.hero2}.{0.skin} on {0.mount}
Pings (STriggerPingEvents):
{1}

Chats (STriggerChatMessageEvents):
{2}

SCmdEvents: {3}
SHeroTalentSelectedEvents: {4}
SCommandManagerTargetPointEvents: {5}
SCameraUpdateEvents: {6}
SUnitClickEvents: {7}
SCommandManagerTargetUnitEvents: {8}
SCommandManagerStateEvents: {9}
'''.format(
    self,
    lf(self.pings),
    lf(self.chats),
    len(self.SCmdEvents),
    # lf(self.SCmdEvents),
    len(self.SHeroTalentSelectedEvents),
    # lf(self.SHeroTalentSelectedEvents),
    len(self.SCommandManagerTargetPointEvents),
    # lf(self.SCommandManagerTargetPointEvents),
    len(self.SCameraUpdateEvents),
    # lf(self.SCameraUpdateEvents),
    len(self.SUnitClickEvents),
    # lf(self.SUnitClickEvents),
    len(self.SCommandManagerTargetUnitEvents),
    # lf(self.SCommandManagerTargetUnitEvents),
    len(self.SCommandManagerStateEvents)
    # lf(self.SCommandManagerStateEvents)
)
