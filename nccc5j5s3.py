import sys
import queue

input = sys.stdin.readline

flights = []
graph = {}

dest, num_flights = [int(i) for i in input().split()]

for _ in range(num_flights):
	a, b = [int(i) for i in input().split()]

	if a in graph:
		graph[a].append(b)
	else:
		graph[a] = [b]

	flights.append((a, b))

for f in flights:
	q = queue.Queue()
	v = []

	if 1 in graph:
		for e in graph[1]:
			q.put((1, e))
			v.append((1, e))

	possible = False

	while not q.empty():
		a, b = q.get()

		if b == dest and (a, b) != f:
			possible = True
			break
		else:
			if (a, b) != f and b in graph:
				for g in graph[b]:
					if (b, g) not in v:
						q.put((b, g))
						v.append((b, g))

	if possible:
		print('YES')
	else:
		print('NO')
