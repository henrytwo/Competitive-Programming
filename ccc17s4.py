b, p, s = [int(i) for i in input().split()]

graph = {}

for _ in range(p):
	a, b, c = [int(i) for i in input().split()]

	if a in graph:
		graph[a].append([b, c])
	else:
		graph[a] = [[b, c]]

print(graph)
