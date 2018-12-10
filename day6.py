import re
from collections import defaultdict


def part1(coords_s):
    coords = []
    for coord in coords_s:
        matched = re.match('(\d+), (\d+)', coord)
        x, y = int(matched.group(1)), int(matched.group(2))
        coords.append((x, y))
    print coords
    min_x = min([x for x, y in coords])
    max_x = max([x for x, y in coords])
    min_y = min([y for x, y in coords])
    max_y = max([y for x, y in coords])
    grid_min_x = min_x - 1
    grid_max_x = max_x + 1
    grid_min_y = min_y - 1
    grid_max_y = max_y + 1
    print (grid_min_x, grid_min_y)
    print (grid_max_x, grid_max_y)

    counter = defaultdict(int)
    for x in range(grid_min_x, grid_max_x):
        coords_to_try = coords
        for y in range(grid_min_y, grid_max_y):
            closest = sorted([(abs(c[0]-x) + abs(c[1]-y), c) for c in coords_to_try], reverse=False)
            if closest[0][0] == closest[1][0]:
                continue
            if closest[0][1][0] in (min_x, max_x) or closest[0][1][1] in (min_y, max_y):
                continue
            counter[closest[0][1]] += 1
    print counter


def part2(coords_s):
    coords = []
    for coord in coords_s:
        matched = re.match('(\d+), (\d+)', coord)
        x, y = int(matched.group(1)), int(matched.group(2))
        coords.append((x, y))
    min_x = min([x for x, y in coords])
    max_x = max([x for x, y in coords])
    min_y = min([y for x, y in coords])
    max_y = max([y for x, y in coords])
    grid_min_x = min_x - 1
    grid_max_x = max_x + 1
    grid_min_y = min_y - 1
    grid_max_y = max_y + 1

    in_region = 0
    LIMIT = 10000
    for x in range(grid_min_x, grid_max_x):
        coords_to_try = coords
        for y in range(grid_min_y, grid_max_y):
            tot_distance = 0
            for c in coords_to_try:
                dist = abs(c[0]-x) + abs(c[1]-y)
                tot_distance += dist
                if tot_distance >= LIMIT:
                    break
            if tot_distance < LIMIT:
                in_region += 1
                print (x, y)
    print in_region
    return in_region



if __name__ == '__main__':
    print(part2("""1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".split('\n')))
#     print(part2("""194, 200
# 299, 244
# 269, 329
# 292, 55
# 211, 63
# 123, 311
# 212, 90
# 292, 169
# 359, 177
# 354, 95
# 101, 47
# 95, 79
# 95, 287
# 294, 126
# 81, 267
# 330, 78
# 202, 165
# 225, 178
# 266, 272
# 351, 326
# 180, 62
# 102, 178
# 151, 101
# 343, 145
# 205, 312
# 74, 193
# 221, 56
# 89, 89
# 242, 172
# 59, 138
# 83, 179
# 223, 88
# 297, 234
# 147, 351
# 226, 320
# 358, 338
# 321, 172
# 54, 122
# 263, 165
# 126, 341
# 64, 132
# 264, 306
# 72, 202
# 98, 49
# 238, 67
# 310, 303
# 277, 281
# 222, 318
# 357, 169
# 123, 225""".split('\n')))
