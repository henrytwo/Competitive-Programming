import sys

input = sys.stdin.readline

num_sheep = int(input())
sheep = []
width = 0

for i in range(num_sheep * 2):
    if i % 2 == 0:
        sheep.append([float(input())])
        if width < sheep[-1][0]:
            width = sheep[-1][0]

    else:
        sheep[-1].append(float(input()))

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

best_dist = 10 ** 10
best_sheep = []
beep = True

while beep:
    for sx, sy in sheep:

        reset = False

        for x in range(0, int(width + 1)):
            d = dist(x, 0, sx, sy)

            if d < best_dist:
                reset = True
                best_dist = d
                best_sheep = [(sx, sy)]
                break

            elif d == best_dist and (sx, sy) not in best_sheep:
                best_sheep.append((sx, sy))

            if [sx, sy] == sheep[-1] and x == width:
                beep = False

        if reset:
            break

for x, y in best_sheep:
    print('The sheep at (%0.2f, %0.2f) might be eaten.' % (x, y))
