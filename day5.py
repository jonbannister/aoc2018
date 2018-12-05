def reduce_s(s):
    s = [_ for _ in s if _ != '\n']
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
            continue
        latest = stack[-1]
        if latest.upper() == c.upper() and c.islower() != latest.islower():
            stack.pop(-1)
        else:
            stack.append(c)
    return stack


def part1(s):
    s = reduce_s(s)
    return len(s)


def part2(s):
    s = reduce_s(s)
    all_chars = list(set(c.upper() for c in s))
    smallest_chain = min(all_chars, key=lambda x: len(reduce_s(''.join(s).replace(x, '').replace(x.lower(), ''))))
    print smallest_chain
    return len(reduce_s(''.join(s).replace(smallest_chain, '').replace(smallest_chain.lower(), '')))


if __name__ == '__main__':
    print(part2(open('./resources/day5.txt').read()))
