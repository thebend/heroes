from HeroBasicTypes import TimePlace

class SUnitDiedEvent:
    def __repr__(self):
        return '{:6} {} - {} > {}'.format(
            '@{}'.format(self.loop),
            self.point,
            self.killerUnitTagIndex,
            self.unitTagIndex
        )
