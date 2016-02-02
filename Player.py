class Player:
    def __init__(self):
        self.SCmdEvents = []
        self.SHeroTalentSelectedEvents = []
        self.SCommandManagerStateEvents = []
        self.SCommandManagerTargetPointEvents = []
        self.SCommandManagerTargetUnitEvents = []
        self.chats = []
        
        # same as actual chats?
        self.STriggerChatMessageEvents = []
        self.STriggerPingEvents = []
        
        self.SUnitClickEvents = []
        self.SCameraUpdateEvents = []

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

SCmdEvents: Omitted
SHeroTalentSelectedEvents: Omitted
SCommandManagerTargetPointEvents: Omitted
SCameraUpdateEvents: Omitted
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
    # Player.lf(self.SCmdEvents),
    # Player.lf(self.SHeroTalentSelectedEvents),
    # Player.lf(self.SCommandManagerTargetPointEvents),
    # Player.lf(self.SCameraUpdateEvents),
)
