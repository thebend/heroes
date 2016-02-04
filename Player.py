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

    @staticmethod
    def lf(data):
        return '\n'.join(str(i) for i in data)

    def __repr__(self):
        return \
'''{} - {:10} ({:8}) | {}.{}.{} on {}
Pings (STriggerPingEvents):
{}

Chats (STriggerChatMessageEvents):
{}

SCmdEvents: {}
SHeroTalentSelectedEvents: {}
SCommandManagerTargetPointEvents: {}
SCameraUpdateEvents: {}
SUnitClickEvents: {}
SCommandManagerTargetUnitEvents: {}
SCommandManagerStateEvents: {}
'''.format(
    self.slot,
    self.name,
    self.id,
    self.hero,
    self.hero2,
    self.skin,
    self.mount,
    Player.lf(self.STriggerPingEvents),
    Player.lf(self.chats),
    len(self.SCmdEvents),
    # Player.lf(self.SCmdEvents),
    len(self.SHeroTalentSelectedEvents),
    # Player.lf(self.SHeroTalentSelectedEvents),
    len(self.SCommandManagerTargetPointEvents),
    # Player.lf(self.SCommandManagerTargetPointEvents),
    len(self.SCameraUpdateEvents),
    # Player.lf(self.SCameraUpdateEvents),
    len(self.SUnitClickEvents),
    # Player.lf(self.SUnitClickEvents),
    len(self.SCommandManagerTargetUnitEvents),
    # Player.lf(self.SCommandManagerTargetUnitEvents),
    len(self.SCommandManagerStateEvents)
    # Player.lf(self.SCommandManagerStateEvents)
)
