import uuid
class Node:
    def __init__(self):
        self.children = []
        self.meta = []
        self.id = uuid.uuid4()
        self.value = 0


def construct(s):
    if not s:
        return
    n_children = s.pop(0)
    n_meta = s.pop(0)
    print(f"{n_children} children, {n_meta} meta")
    this = Node()
    for child in range(n_children):
        this.children.append(construct(s))
    for i in range(n_meta):
        this.meta.append(s.pop(0))
    return this


def part1(s):
    tree = construct(s)
    visited = set()
    to_visit = [tree]
    meta_ct = 0
    while to_visit:
        curr = to_visit.pop(0)
        visited.add(curr.id)
        meta_ct += sum(curr.meta)
        to_visit.extend([c for c in curr.children if c.id not in visited])
    return meta_ct


def part2(s):
    tree = construct(s)
    visited = set()
    to_visit = [tree]
    while to_visit:
        curr = to_visit.pop(0)
        print(f"visiting node with {len(curr.children)} children and {len(curr.meta)} meta")
        if not curr.children:
            curr.value = sum(curr.meta)
            visited.add(curr.id)
        to_visit.extend([c for c in curr.children if c.id not in visited])
        if curr.children:
            if all(x.id in visited for x in curr.children):
                total = 0
                for x in curr.meta:
                    if len(curr.children) >= x:
                        total += curr.children[x-1].value
                curr.value = total
                visited.add(curr.id)
            else:
                to_visit.append(curr)
    return tree.value



if __name__ == '__main__':
    # print(part2([int(i) for i in """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2""".split(" ")]))
    print(part2([int(i) for i in open('./resources/day8.txt').read().split(" ")]))