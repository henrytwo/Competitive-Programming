import sys
import queue

input = sys.stdin.readline

h, w = [int(i) for i in input().split()]

cam_queue = queue.Queue()
grid = []
space = []
dists = []
sx, sy = 9999, 9999

moves = {'U':(0, -1), 'D':(0, 1), 'L':(-1, 0), 'R':(1, 0)}
pos = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for y in range(h):
    grid.append(list(input()))

    for x in range(len(grid[-1])):
        if grid[-1][x] == '.':
            space.append((x, y))
            dists.append(-1)
        elif grid[-1][x] == 'S':
            sx, sy = x, y
        elif grid[-1][x] == 'C':
            grid[-1][x] = 'W'

            cam_queue.put((x, y, 'A'))

while not cam_queue.empty():
    x, y, d = cam_queue.get()

    if grid[y][x] == '.':
        grid[y][x] = 'X'

    if (d == 'E' or d == 'A') and x + 1 < w and (grid[y][x + 1] == '.' or grid[y][x + 1] in moves or grid[y][x + 1] == 'X'):
        cam_queue.put((x + 1, y, 'E'))

    if (d == 'W' or d == 'A') and x - 1 > 0 and (grid[y][x - 1] == '.' or grid[y][x - 1] in moves or grid[y][x + 1] == 'X'):
        cam_queue.put((x - 1, y, 'W'))

    if (d == 'N' or d == 'A') and y + 1 < h and (grid[y + 1][x] == '.' or grid[y + 1][x] in moves or grid[y][x + 1] == 'X'):
        cam_queue.put((x, y + 1, 'N'))

    if (d == 'S' or d == 'A') and y - 1 > 0 and (grid[y - 1][x] == '.' or grid[y - 1][x] in moves or grid[y][x + 1] == 'X'):
        cam_queue.put((x, y - 1, 'S'))

#for line in grid:
#    print(line)

q = queue.Queue()
q.put((-1, sx, sy, 0))

while not q.empty():
    i, x, y, d = q.get()

    if (x, y) in space:
        dists[i] = d

    grid[y][x] = 'W'

    if (x + 1, y) in space and grid[y][x + 1] == '.':
        q.put((space.index((x + 1, y)), x + 1, y, d + 1))

    if (x - 1, y) in space and grid[y][x - 1] == '.':
        q.put((space.index((x - 1, y)), x - 1, y, d + 1))

    if (x, y + 1) in space and grid[y][x] == '.':
        q.put((space.index((x, y + 1)), x, y + 1, d + 1))

    if (x, y - 1) in space and grid[y - 1][x] == '.':
        q.put((space.index((x, y - 1)), x, y - 1, d + 1))

    for x_off, y_off in pos:
        if 0 < x + x_off < w and 0 < y + y_off < h and grid[y_off + y][x_off + x] in moves:
            mx, my = moves[grid[y_off + y][x_off + x]]

            if 0 < mx + x_off + x < w and 0 < my + y_off + y < h and grid[my + y_off + y][mx + x_off + x] == '.':
                if (mx + x_off + x, my + y_off + y) in space:
                    meh = space.index((mx + x_off + x, my + y_off + y))
                else:
                    meh = -1

                q.put((meh, mx + x_off + x, my + y_off + y, d + 1))

            elif 0 < mx + x_off + x < w and 0 < my + y_off + y < h and grid[my + y_off + y][mx + x_off + x] in moves:
                q.put((-1, mx + x_off + x, my + y_off + y, d))

print('\n'.join(list(map(str, dists))))
