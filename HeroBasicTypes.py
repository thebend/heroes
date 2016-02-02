class TimePlace:
    @staticmethod
    def from_json(json, point_key):
        loop = json['_gameloop']
        t = json[point_key]
        if t == None:
            return TimePlace(loop, None)
        try: z = t['z']
        except KeyError: z = None
        point = Point(t['x'], t['y'], z)
        return TimePlace(loop, point)

    def __init__(self, loop, location):
        self.loop = loop
        self.location = location

    def __repr__(self):
        return '{:>6} {}'.format(
            '@{}'.format(self.loop),
            self.location
        )

class Point:
    def __init__(self, x, y, z = None):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        if self.z == None:
            return '({:6}, {:6})'.format(
                self.x,
                self.y
            )
        else:
            return '({:6}, {:6}, {:6})'.format(
                self.x,
                self.y,
                self.z
            )

class Chat:
    def __repr__(self):
        return '{:6}: {}'.format(
            '@{}'.format(self.loop),
            self.message
        )

class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __repr__(self):
        return '({},{},{},{})'.format(
            self.r,
            self.g,
            self.b,
            self.a
        )
