import queue

thicc, num_island, num_path = list(map(int, input().split()))

graph = {}
d = [-1 for _ in range(num_island)]
q = queue.PriorityQueue()

for p in range(num_path):
	s, e, t, w = list(map(int, input().split()))
	if (s - 1) in graph:
		if e - 1 in graph[s - 1]:
			graph[s - 1][e - 1].append([t, w])
		else:
			graph[s - 1][e - 1] = [[t, w]]
	else:
		graph[s - 1] = {e - 1 : [[t, w]]}

	if (e - 1) in graph:
		if s - 1 in graph[e - 1]:
			graph[e - 1][s - 1].append([t, w])
		else:
			graph[e - 1][s - 1] = [[t, w]]
	else:
		graph[e - 1] = {s - 1: [[t, w]]}

start, target = list(map(int, input().split()))

#print(graph)

q.put((0, start - 1, thicc))

while not q.empty():

	t, n, w = q.get()

	#print('Goto', n + 1, ' Time', t, ' Thicc', w)
	if d[n] == -1 or t < d[n]:
		d[n] = t

		if n == target - 1:
			#print("bro" + str(t))
			break

		if n in graph: # Find node
			for tar in graph[n]: # Destinations
				for node in graph[n][tar]: # Routes
					#print('NODE', node)
					if w - node[1] > 0:
						q.put((node[0] + t, tar, w - node[1]))

	#print(d)

#print(d)
print(d[target - 1])
