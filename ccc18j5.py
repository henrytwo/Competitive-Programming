import sys

input = sys.stdin.readline

num_pages = int(input())

graph = {}
visited = {1}
shortest = 10**10

for page in range(num_pages):
	pineapple = list(map(int, input().split()))

	if pineapple[0] > 0:
		graph[page + 1] = pineapple[1:]
	else:
		graph[page + 1] = []

def rec(steps, tar):

	global shortest
	if tar in graph:
		if len(graph[tar]) == 0:
			if steps < shortest:
				shortest = steps

		else:
			for t in graph[tar]:
				if t not in visited:
					rec(steps + 1, t)
					visited.add(t)

rec(1, 1)

if len(visited) == num_pages:
	print('Y')
else:
	print('N')

print(shortest)
