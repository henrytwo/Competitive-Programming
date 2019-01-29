import sys
import queue

input = sys.stdin.readline

W, H, N = [int(i) for i in input().split()]

#H += 1
#W += 1

#grid = [[0 for _ in range(H)] for __ in range(W)]

start = [int(i) for i in input().split()]
end = [int(i) for i in input().split()]

wind = []

for _ in range(N):
	wind.append([int(i) for i in input().split()])

q = queue.Queue()
q.put([start, [], 0, None, 0])

positions = [[0, 1], [1, 0], (0, -1), (-1, 0)]

visited = {tuple(start)}

def on_grid(x, y):
	return 0 <= x <= W and 0 <= y <= H

found = False

while not q.empty():
	location, past, time, prev, pc = q.get()

	x, y = location

	if location == end:
		found = True
		print(time)
		break

	for pos in positions:
		if on_grid(x + pos[0], y + pos[1]) and (x + pos[0], y + pos[1]) not in visited and [x + pos[0], y + pos[1]] not in wind:

			d_t = time
			d_pc = pc

			if (prev != pos and prev) or [x + pos[0], y + pos[1]] == end:
				d_t += d_pc + 1

				if [x + pos[0], y + pos[1]] and d_pc in [0, 1]:
					d_t += d_pc + 1

				#print('swap', d_t, d_pc, [x + pos[0], y + pos[1]])

				d_pc = 1
			else:
				d_pc += 1

				#print('add', d_t, d_pc, [x + pos[0], y + pos[1]])

			q.put([[x + pos[0], y + pos[1]], past[:] + [location], d_t, pos, d_pc])
			visited.add((x + pos[0], y + pos[1]))
if not found:
	print(-1)
