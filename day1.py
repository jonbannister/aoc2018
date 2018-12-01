import itertools


def apply_freq(change):
    sign, n = change[0], int(change[1:])
    return -n if sign == '-' else n


def part1(s):
    freq = 0
    for change in s.split('\n'):
        freq += apply_freq(change)
    return freq


def part2(s):
    seen_frequencies = set()
    freq = 0
    for change in itertools.cycle(s.split('\n')):
        freq += apply_freq(change)
        if freq in seen_frequencies:
            return freq
        seen_frequencies.add(freq)


if __name__ == '__main__':
    print(part2('''+7
    +7
    -2
    -7
    -4'''))

