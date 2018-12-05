def reduce_s(s):
    s = [_ for _ in s if _ != '\n']
    while True:
        n_removed = 0
        to_inspect = [0]
        for i in to_inspect:
            if i >= len(s)-1:
                break
            done_something = False
            if s[i].islower() != s[i+1].islower() and s[i].upper() == s[i+1].upper():
                s = s[:i] + s[i+2:]
                n_removed += 1
                if i+1 < len(s):
                    to_inspect.append(i)
            elif i > 0 and s[i].islower() != s[i-1].islower() and (s[i].upper() == s[i-1].upper()):
                s = s[:i-1] + s[i+1:]
                n_removed += 1
                if 0 < i-1 < len(s):
                    to_inspect.append(i-1)
                else:
                    to_inspect.append(0)

            elif not done_something and i+1 < len(s):
                to_inspect.append(i+1)

        if n_removed == 0:
            break
    return s


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
