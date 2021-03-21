import sys

def straight_lines(puzzle: list, rows: int, cols: int) -> dict:
    d = dict()

    # key is coord
    # value is another dict
    # keys of that dict are 'up' 'down' 'left' and 'right'
    # values of that dict are lists of the number of length sequences that are in them. Can have dupes for 2 in one direction, and 2 in another.

    for row in range(rows):
        for col in range(cols):
            if puzzle[row][col] == 1:

                max_len_up = 0
                while (row - max_len_up >= 0):
                    if puzzle[row - max_len_up][col] == 1:
                        max_len_up += 1
                    else:
                        break

                max_len_down = 0
                while (row + max_len_down < rows):
                    if puzzle[row + max_len_down][col] == 1:
                        max_len_down += 1
                    else:
                        break

                max_len_left = 0
                while (col - max_len_left >= 0):
                    if puzzle[row][col - max_len_left] == 1:
                        max_len_left += 1
                    else:
                        break

                max_len_right = 0
                while (col + max_len_right < cols):
                    if puzzle[row][col + max_len_right] == 1:
                        max_len_right += 1
                    else:
                        break

                d[(row, col)] = {'u': max_len_up, 'd': max_len_down, 'l': max_len_left, 'r': max_len_right}
    return d

def get_num_ls(d: dict):
    num_ls = 0

    # For all possible endpoints
    for k, v in d.items():

        if v['u'] >= 4:
            # for all even lengths greater than 4.
            for i in range(1, v['u'] // 2):
                l = i * 2
                if v['l'] > i:
                    num_ls += 1
                if v['r'] > i:
                    num_ls += 1
        if v['d'] >= 4:
            # for all even lengths greater than 4.
            for i in range(1, v['d'] // 2):
                l = i * 2
                if v['l'] > i:
                    num_ls += 1
                if v['r'] > i:
                    num_ls += 1
        if v['l'] >= 4:
            # for all even lengths greater than 4.
            for i in range(1, v['l'] // 2):
                l = i * 2
                if v['u'] > i:
                    num_ls += 1
                if v['d'] > i:
                    num_ls += 1
        if v['r'] >= 4:
            # for all even lengths greater than 4.
            for i in range(1, v['r'] // 2):
                l = i * 2
                if v['u'] > i:
                    num_ls += 1
                if v['d'] > i:
                    num_ls += 1

    return num_ls


a = []
for line in sys.stdin:
    a.append(line.strip())

num_puzzles = int(a[0])
head = 1
for p in range(num_puzzles):
    rows = int(a[head].split(' ')[0])
    cols = int(a[head].split(' ')[1])

    puzzle = []
    for x in range(1, rows+1):
        puzzle.append([int(x) for x in a[head+x].split(' ')])

    lines = straight_lines(puzzle, rows, cols)
    num_ls = get_num_ls(lines)

    print("Case #{}: {}".format(p + 1, num_ls))

    head += rows+1
    