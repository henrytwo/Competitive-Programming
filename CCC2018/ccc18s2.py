import sys
import copy
input = sys.stdin.readline

num_flower = int(input())

data = []

for _ in range(num_flower):
    data.append(list(map(int, input().split())))

def slice(grid, col):
    export = []

    for y in grid:
        export.append(y[col])

    return export

def validator(grid):

    begin = slice(copy.deepcopy(grid), 0);
    end = slice(copy.deepcopy(grid), len(grid) - 1)

    sorted_begin = sorted(begin)
    sorted_end = sorted(end)

    if begin != sorted_begin:
        return False

    begin_index = []
    end_index = []

    for line in grid:
        if line[0] > line[-1]:
            return False

    for num in sorted_begin:
        begin_index.append(begin.index(num))
        begin[begin.index(num)] = 10**10

    for num in sorted_end:
        end_index.append(end.index(num))
        end[end.index(num)] = 10**10

    return begin_index == end_index

def rotate(grid):
    new_grid = [[0 for __ in range(len(grid[0]))] for _ in range(len(grid))]

    for x in range(len(grid)):
        for y in range(len(grid)):
            new_grid[x][y] = grid[len(grid) - y - 1][len(grid) - x - 1]

        new_grid[x] = new_grid[x][::-1]

    return new_grid

for i in range(4):
    valid = validator(data)

    if not valid:
        data = rotate(data)
    else:
        break

for line in data:
    print(" ".join(list(map(str, line))))
