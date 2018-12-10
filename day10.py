import re

class Point(object):
    def __init__(self, x, y, v_x, v_y):
        self.x = int(x)
        self.y = int(y)
        self.v_x = int(v_x)
        self.v_y = int(v_y)

    def apply(self):
        self.x += self.v_x
        self.y += self.v_y

    def __repr__(self):
        return "Point({}, {} travelling ({}, {}))".format(self.x, self.y, self.v_x, self.v_y)


def part1and2(pts):
    points = []
    all_points = set()
    for pt in pts:
        print pt
        m = re.match(r"position=< ?(-?\d+).*, +?(-?\d+)> velocity=< ?(-?\d+).*, +?(-?\d+)>", pt)
        p = Point(*m.groups())
        print(p)
        points.append(p)
        all_points.add((p.x, p.y))

    seconds = 0
    while True:

        xmin = min(points, key=lambda p: p.x).x
        ymin = min(points, key=lambda p: p.y).y
        xmax = max(points, key=lambda p: p.x).x
        ymax = max(points, key=lambda p: p.y).y

        if xmin > 150 and ymin > 160:

            for y in range(ymin, ymax + 1):
                s = ''
                for x in range(xmin, xmax+1):
                    if (x, y) in all_points:
                        s += '#'
                    else:
                        s += '.'
                print(s)

            i = raw_input('More? n for no (min=({}, {}), max=({}, {}), seconds={})\n'.format(xmin, ymin, xmax, ymax, seconds))
            if i == "n":
                break
        all_points = set()
        for p in points:
            p.apply()
            all_points.add((p.x, p.y))
        seconds += 1


if __name__ == '__main__':
    part1and2(open("./resources/day10.txt").read().strip().split('\n'))
