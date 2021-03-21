import sys
from collections import defaultdict

def get_boxes_in_puzzle(puzzle: list) -> int:
    return sum([x for y in puzzle for x in y])

def manhatten_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def create_safe_puzzle(puzzle: list) -> list:
    rows = len(puzzle)
    cols = len(puzzle[0])

    locs_not_to_try = set()
    d = defaultdict(list)

    for r in range(rows):
        for c in range(cols):
            d[puzzle[r][c]].append((r, c))

    l = list(d.items())
    l.sort(key=lambda x: -x[0])

    for h in l:
        for r, c in h[1]:
            if (r, c) not in locs_not_to_try:
                v = puzzle[r][c]
                for r2 in range(rows):
                    for c2 in range(cols):
                        current_value = puzzle[r2][c2]
                        min_safe_value = v - manhatten_dist((r, c), (r2, c2))
                        if min_safe_value >= current_value:
                            puzzle[r2][c2] = min_safe_value
                            locs_not_to_try.add((r2, c2))
    return puzzle


a = []
for line in sys.stdin:
    a.append(line.strip())

num_houses = int(a[0])
head = 1
for h in range(num_houses):
    rows = int(a[head].split(' ')[0])
    cols = int(a[head].split(' ')[1])

    puzzle = []
    for x in range(1, rows+1):
        puzzle.append([int(x) for x in a[head+x].split(' ')])

    num_boxes = get_boxes_in_puzzle(puzzle)
    safe_puzzle = create_safe_puzzle(puzzle)
    
    safe_boxes = get_boxes_in_puzzle(safe_puzzle)
    print("Case #{}: {}".format(h+1, safe_boxes - num_boxes))

    head += rows+1
