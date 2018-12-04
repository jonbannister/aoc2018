import datetime
import re
from collections import defaultdict


def get_solution(shifts_s):
    shifts = sorted([x for x in shifts_s.split('\n') if x], key=lambda s: datetime.datetime.strptime(s[1:17], '%Y-%m-%d %H:%M'))
    current_guard = None
    sleep_time = None
    laziness = defaultdict(lambda: defaultdict(int))
    while shifts:
        curr = shifts.pop(0)
        if 'begins shift' in curr:
            current_guard = re.match('.*Guard #(\d+) begins shift', curr).group(1)
            continue
        timestamp = datetime.datetime.strptime(curr[1:17], '%Y-%m-%d %H:%M')
        if 'falls asleep' in curr:
            sleep_time = timestamp
        elif 'wakes up' in curr:
            timestamp -= datetime.timedelta(minutes=1)
            while timestamp >= sleep_time:
                laziness[current_guard][timestamp.minute] += 1
                timestamp -= datetime.timedelta(minutes=1)
            sleep_time = None
        else:
            print "WHAT"
    return laziness


def part1(shifts_s):
    laziness = get_solution(shifts_s)
    most_lazy = max(laziness, key=lambda d: sum(laziness[d].values()))
    highest_freq = max(laziness[most_lazy], key=lambda d: laziness[most_lazy][d])
    return int(most_lazy) * int(highest_freq)


def part2(shifts_s):
    laziness = get_solution(shifts_s)
    most_consistent_guard = max(laziness, key=lambda d: max(laziness[d].values()))
    highest_freq = max(laziness[most_consistent_guard], key=lambda d: laziness[most_consistent_guard][d])
    return int(most_consistent_guard) * int(highest_freq)


if __name__ == '__main__':
    print(part2(open('./resources/day4.txt').read()))
