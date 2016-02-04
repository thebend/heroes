from collections import namedtuple

Color = namedtuple('Color','r g b a')
Color.__repr__ = lambda self: '({},{},{},{})'.format(
    self.r, self.g, self.b, self.a
)

TimePlace = namedtuple('TimePlace', 'loop point')
TimePlace.__repr__ = lambda self: '{:>6} {}'.format(
    '@{}'.format(self.loop),
    self.point
)
def json_timeplace(json, point_key):
    loop = json['_gameloop']
    t = json[point_key]
    point = None if t == None else Point(t)
    return TimePlace(loop, point)

class Point:
    def __init__(self, x, y = None, z = None):
        # x can actually be dictionary of whole point
        if type(x) == dict:
            self.x, self.y = x['x'], x['y']
            try: self.z = x['z']
            except KeyError: self.z = None
        else:
            self.x, self.y, self.z = x, y, z

    def __repr__(self):
        if self.z == None: return '({:6}, {:6})'.format(self.x, self.y)
        return '({:6}, {:6}, {:6})'.format(self.x, self.y, self.z)
