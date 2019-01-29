import sys
import queue

input = sys.stdin.readline

locations, num_portals, locker, math = [int(i) for i in input().split()]

portals = []
time = -1

for _ in range(num_portals):
	portals.append([int(i) for i in input().split()])
	portals.append(portals[-1][::-1])

q = queue.Queue()
q.put([1, 0, False])

visited = set()
gotem = False
while not q.empty():
	node, time, hazlocker = q.get()

	if node == math and hazlocker:
		print(time)
		gotem = True
		break

	visited.add(node)

	for p in portals:
		if p[0] == node and p[1] not in visited:
			if p[1] == locker:
				visited = {p[1]}
			q.put([p[1], time + 1, p[1] == locker or hazlocker])

if not gotem:
	print(-1)
