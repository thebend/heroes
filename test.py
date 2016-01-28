import HeroParser

replay_path = r'C:\heroes\replays\ben\zag1.StormReplay'
replay = HeroParser.HeroParser(replay_path)
details = replay.get_game_events()
details = list(details)
print type(details[0])
print len(details)
