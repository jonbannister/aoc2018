import itertools
import re
from collections import defaultdict


def part1(commands):
    occupied = defaultdict(int)
    for command in commands.split('\n'):
        if not command:
            continue
        regex_match = re.match('#.* (\d+),(\d+): (\d+)x(\d+)', command)
        startx, starty, width, height = regex_match.groups()
        startx, starty, width, height = [int(x) for x in (startx, starty, width, height)]
        all_targets = [(startx+x, starty+y) for (x, y) in itertools.product(range(width), range(height))]
        for target in all_targets:
            occupied[target] += 1
    return sum(1 for x in occupied.values() if x > 1)


def part2(commands):
    occupied = defaultdict(int)
    cmd_to_targets = {}
    for command in commands.split('\n'):
        if not command:
            continue
        regex_match = re.match('#.* (\d+),(\d+): (\d+)x(\d+)', command)
        startx, starty, width, height = regex_match.groups()
        startx, starty, width, height = [int(x) for x in (startx, starty, width, height)]
        all_targets = [(startx+x, starty+y) for (x, y) in itertools.product(range(width), range(height))]
        cmd_to_targets[command] = all_targets
        for target in all_targets:
            occupied[target] += 1
    for command in commands.split('\n'):
        regex_match = re.match('#(\d+).* (\d+),(\d+): (\d+)x(\d+)', command)
        n, startx, starty, width, height = regex_match.groups()
        n = int(n)
        all_targets = cmd_to_targets[command]
        if sum(occupied[t] for t in all_targets ) == len(all_targets):
            return n


if __name__ == '__main__':
    print(part1(open('./resources/day3.txt').read()))
