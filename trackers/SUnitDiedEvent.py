from HeroBasicTypes import TimePlace, Point
from TrackerProcessor import TrackerProcessor

class SUnitDiedEvent:
    def __repr__(self):
        return '{:6} {} - {} > {}'.format(
            '@{}'.format(self.loop),
            self.point,
            self.killerUnitTagIndex,
            self.unitTagIndex
        )

@TrackerProcessor(2)
def get(game, tracker):
    ud = SUnitDiedEvent()
    ud.timeplace = TimePlace(
        tracker['_gameloop'],
        Point(tracker['m_x'], tracker['m_y'])
    )
    ud.killer_player_id = tracker['m_killerPlayerId']
    ud.killerUnitTagIndex = tracker['m_killerUnitTagIndex']
    ud.unitTagIndex = tracker['m_unitTagIndex']
    game.deaths.append(ud)