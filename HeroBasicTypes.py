from collections import namedtuple

Color = namedtuple('Color','r g b a')
Color.__repr__ = lambda self: '({0.r},{0.g},{0.b},{0.a})'.format(self)

TimePlace = namedtuple('TimePlace', 'loop point')
TimePlace.__repr__ = lambda self: '{:>6} {}'.format(
    '@{}'.format(self.loop),
    self.point
)
def json_timeplace(json, point_key):
    t = json[point_key]
    return TimePlace(
        loop = json['_gameloop'],
        point = None if t == None else Point(t)
    )


class Point:
    def __init__(self, x, y = None, z = None):
        # x can actually be dictionary of whole point
        if type(x) == dict:
            self.x = x['x']
            self.y = x['y']
            try: self.z = x['z']
            except KeyError: self.z = None
        else:
            self.x, self.y, self.z = x, y, z

    def __repr__(self):
        if self.z == None: return '({0.x:6}, {0.y:6})'.format(self)
        return '({0.x:6}, {0.y:6}, {0.z:6})'.format(self)
