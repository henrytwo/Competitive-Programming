import sys
input = sys.stdin.readline

graph = {}

num_city = int(input())

for n in range(1, num_city):
	o = int(input())

	if o in graph:
		graph[o].append(n)
	else:
		graph[o] = [n]

print(graph)
