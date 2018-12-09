from collections import defaultdict


class DoublyNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None


def part1(n_players, max_marble):
    marbles = [0]
    scores = defaultdict(int)
    c_player = 0
    c_marble_idx = 0
    c_marble_no = 1
    while c_marble_no <= max_marble:
        c_player += 1
        if c_player > n_players:
            c_player -= n_players
        if c_marble_no % 23 == 0:
            c_marble_idx -= 7
            if c_marble_idx < 0:
                c_marble_idx += len(marbles)
            value = marbles.pop(c_marble_idx)
            scores[c_player] += value + c_marble_no
        else:
            start = c_marble_idx + 1
            if start == len(marbles):
                start = 0
            marbles.insert(start+1, c_marble_no)
            c_marble_idx = start+1
        c_marble_no += 1
    print(max(scores.values()))


def part2(n_players, max_marble):
    c_marble = DoublyNode(0)
    c_marble.prev = c_marble
    c_marble.next = c_marble
    scores = defaultdict(int)
    c_player = 0
    c_marble_no = 1
    while c_marble_no <= max_marble:
        c_player += 1
        if c_player > n_players:
            c_player -= n_players
        if c_marble_no % 23 == 0:
            for _ in range(7):
                c_marble = c_marble.prev
            m_to_remove = c_marble
            m_to_remove.prev.next = m_to_remove.next
            m_to_remove.next.pre = m_to_remove.prev
            c_marble = m_to_remove.next
            scores[c_player] += m_to_remove.value + c_marble_no
            del m_to_remove
        else:
            new_marble = DoublyNode(c_marble_no)
            new_marble.prev = c_marble.next
            new_marble.next = c_marble.next.next
            c_marble.next.next.prev = new_marble
            c_marble.next.next = new_marble
            c_marble = new_marble

        c_marble_no += 1
    print(max(scores.values()))



if __name__ == '__main__':
    # part2(21, 6111)
    part2(439, 7130700)