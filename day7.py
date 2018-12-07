from typing import Tuple, Dict
import re


class Node(object):
    def __init__(self, label):
        self.label = label
        self.parents = []
        self.children = []

    def add_child(self, child: 'Node') -> None:
        self.children.append(child)

    def add_parent(self, parent: 'Node') -> None:
        self.parents.append(parent)

    def __repr__(self):
        return f"Node({[x.label for x in self.parents]} -> {self.label} -> {[x.label for x in self.children]})"


def build_graph(s: str) -> Dict[str, Node]:
    nodes = {}
    for instruction in s.split('\n'):
        regex = re.match('Step ([A-Z]+) must.*before step ([A-Z]+).*', instruction)
        if not regex:
            continue
        step_before, step_after = regex.groups()
        print(step_before, step_after)
        after = nodes.get(step_after, Node(step_after))
        before = nodes.get(step_before, Node(step_before))
        before.add_child(after)
        after.add_parent(before)
        nodes[step_before] = before
        nodes[step_after] = after
    return nodes


def part1(s: str) -> str:
    graph = build_graph(s)
    visited = set()
    traversal_order = []
    to_traverse = [node for node in graph.values() if not node.parents]
    to_traverse = sorted(to_traverse, key=lambda node: node.label)
    while to_traverse:
        current = to_traverse.pop(0)
        if current.label in visited:
            continue
        traversal_order.append(current.label)
        visited.add(current.label)
        for child in current.children:
            if child.label not in visited and all(parent.label in visited for parent in child.parents):
                to_traverse.append(child)
        to_traverse = sorted(to_traverse, key=lambda node: node.label)
        print(f'Visited {current.label}, now to_traverse = {to_traverse}')
    return ''.join(traversal_order)


def letter_to_time(c: str) -> int:
    return ord(c) - 4

def part2(s: str) -> int:
    graph = build_graph(s)
    visited = set()
    to_traverse = [node for node in graph.values() if not node.parents]
    to_traverse = sorted(to_traverse, key=lambda node: node.label)
    n_workers = 5
    start_times = {}
    workers = {}
    current_time = 0
    while True:
        for id, work in workers.items():
            if work is None:

                print(f'{current_time}: Worker {id} did nothing')
            elif current_time == start_times[id]+letter_to_time(work.label):
                visited.add(work.label)
                for child in work.children:
                    if child.label not in visited and child not in to_traverse:
                        to_traverse.append(child)
                to_traverse = sorted(to_traverse, key=lambda node: node.label)
                print(f'{current_time}: Worker {id} Visited {work.label}, now to_traverse = {to_traverse}')
                workers[id] = None
            else:
                print(f'{current_time}: Worker {id} is still working on {work.label}')
        reachable = [node for node in to_traverse if all(parent.label in visited for parent in node.parents)]
        for n in range(n_workers):
            if reachable and not workers.get(n):
                to_do = to_traverse.pop(to_traverse.index(reachable.pop(0)))
                if to_do.label in visited:
                    continue
                workers[n] = to_do
                start_times[n] = current_time
                print(f'Worker {n} started working on {workers[n].label}. It should finish at {current_time + letter_to_time(workers[n].label)}')
        if not to_traverse and not sum(1 for x in workers.values() if x):
            break
        current_time += 1
    return current_time


if __name__ == '__main__':
    print(part2("""Step I must be finished before step G can begin.
Step J must be finished before step A can begin.
Step L must be finished before step D can begin.
Step V must be finished before step S can begin.
Step U must be finished before step T can begin.
Step F must be finished before step Z can begin.
Step D must be finished before step A can begin.
Step E must be finished before step Z can begin.
Step C must be finished before step Q can begin.
Step H must be finished before step X can begin.
Step A must be finished before step Z can begin.
Step Z must be finished before step M can begin.
Step P must be finished before step Y can begin.
Step N must be finished before step K can begin.
Step R must be finished before step W can begin.
Step K must be finished before step O can begin.
Step W must be finished before step S can begin.
Step G must be finished before step Q can begin.
Step Q must be finished before step B can begin.
Step S must be finished before step T can begin.
Step B must be finished before step M can begin.
Step T must be finished before step Y can begin.
Step M must be finished before step O can begin.
Step X must be finished before step O can begin.
Step O must be finished before step Y can begin.
Step C must be finished before step O can begin.
Step B must be finished before step O can begin.
Step T must be finished before step O can begin.
Step S must be finished before step X can begin.
Step E must be finished before step K can begin.
Step Q must be finished before step M can begin.
Step E must be finished before step P can begin.
Step Q must be finished before step S can begin.
Step E must be finished before step O can begin.
Step D must be finished before step P can begin.
Step X must be finished before step Y can begin.
Step I must be finished before step U can begin.
Step B must be finished before step X can begin.
Step F must be finished before step T can begin.
Step B must be finished before step T can begin.
Step V must be finished before step R can begin.
Step I must be finished before step Q can begin.
Step I must be finished before step A can begin.
Step M must be finished before step X can begin.
Step Z must be finished before step S can begin.
Step C must be finished before step S can begin.
Step T must be finished before step M can begin.
Step K must be finished before step X can begin.
Step Z must be finished before step P can begin.
Step V must be finished before step H can begin.
Step Z must be finished before step B can begin.
Step M must be finished before step Y can begin.
Step C must be finished before step K can begin.
Step W must be finished before step Y can begin.
Step J must be finished before step Z can begin.
Step Q must be finished before step O can begin.
Step T must be finished before step X can begin.
Step P must be finished before step Q can begin.
Step P must be finished before step K can begin.
Step D must be finished before step M can begin.
Step P must be finished before step N can begin.
Step S must be finished before step B can begin.
Step H must be finished before step Y can begin.
Step R must be finished before step K can begin.
Step G must be finished before step S can begin.
Step P must be finished before step S can begin.
Step C must be finished before step Z can begin.
Step Q must be finished before step Y can begin.
Step F must be finished before step R can begin.
Step N must be finished before step B can begin.
Step G must be finished before step M can begin.
Step E must be finished before step X can begin.
Step D must be finished before step E can begin.
Step D must be finished before step C can begin.
Step U must be finished before step O can begin.
Step H must be finished before step Z can begin.
Step L must be finished before step C can begin.
Step L must be finished before step F can begin.
Step V must be finished before step D can begin.
Step F must be finished before step X can begin.
Step V must be finished before step W can begin.
Step S must be finished before step Y can begin.
Step K must be finished before step T can begin.
Step D must be finished before step Z can begin.
Step C must be finished before step W can begin.
Step V must be finished before step M can begin.
Step F must be finished before step H can begin.
Step A must be finished before step M can begin.
Step G must be finished before step Y can begin.
Step H must be finished before step M can begin.
Step N must be finished before step W can begin.
Step J must be finished before step K can begin.
Step C must be finished before step B can begin.
Step Z must be finished before step Y can begin.
Step L must be finished before step E can begin.
Step G must be finished before step B can begin.
Step Q must be finished before step T can begin.
Step D must be finished before step W can begin.
Step H must be finished before step G can begin.
Step L must be finished before step O can begin.
Step N must be finished before step O can begin."""))
