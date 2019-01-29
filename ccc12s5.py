import sys
import queue

input = sys.stdin.readline

w, h = [int(x) for x in input().strip().split()]

map = [[0 for _ in range(h)] for __ in range(w)]

for _ in range(int(input())):
	x, y = [int(x) - 1 for x in input().strip().split()]
	map[x][y] = 'X'

q = queue.Queue()

hai = set()
q.put((1, 1))

map[0][0] = 1

while not q.empty():
	x, y = q.get()

	if x - 1 > -1 and map[x - 1][y] != 'X':
		map[x][y] += map[x - 1][y]

	if y - 1 > -1 and map[x][y - 1] != 'X':
		map[x][y] += map[x][y - 1]

	if x + 1 < len(map) and map[x + 1][y] != 'X' and (x + 1, y) not in hai:
		q.put((x + 1, y))
		hai.add((x + 1, y))

	if y + 1 < len(map) and map[x][y + 1] != 'X' and (x, y + 1) not in hai:
		q.put((x, y + 1))
		hai.add((x, y + 1))

for line in map:
	print(line)

