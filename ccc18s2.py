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

    begin_index = []
    end_index = []

    for num in sorted_begin:
        begin_index.append(begin.index(num))
        begin[begin.index(num)] = 10**10

    for num in sorted_end:
        end_index.append(end.index(num))
        end[end.index(num)] = 10**10

    return sorted_begin == sorted_end

print(validator([[1, 3], [2,9]]))
