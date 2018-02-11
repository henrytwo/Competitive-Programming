import queue
import sys

input = sys.stdin.readline

floor = int(input())
rows = int(input())
cols = int(input())

g = []
empty = 0

for line in range(rows):
	line = input()
	g.append(list(line))
	empty += line.count('.')

s = g[:]

c = []
visited = []

q = queue.Queue()
room = -1

def search():
	global room

	room += 1

	found = False

	for y in range(len(s)):

		if found:
			break

		for x in range(len(s[y])):
			if s[y][x] == '.' and [y, x] not in visited:
				q.put([y, x])
				
				visited.append([y, x])
				found = True
				break

while len(visited) < empty:

	search()

	while not q.empty():
		y, x = q.get()

		if room < len(c):
			c[room] += 1
		else:
			c.append(1)

		if x + 1 < cols and [y, x + 1] not in visited and s[y][x + 1] == '.':
			visited.append([y, x + 1])
			q.put([y, x + 1])

		if x - 1 > 0 and [y, x - 1] not in visited and s[y][x - 1] == '.':
			visited.append([y, x - 1])
			q.put([y, x - 1])

		if y + 1 < rows and [y + 1, x] not in visited and s[y + 1][x] == '.':
			visited.append([y + 1, x])
			q.put([y + 1, x])

		if y - 1 > 0 and [y - 1, x] not in visited and s[y - 1][x] == '.':
			visited.append([y - 1, x])
			q.put([y - 1, x])

c.sort()
num_rm = 0

for rm in c[::-1]:
	if floor - rm > 0:
		floor -= rm
		num_rm += 1
	else:
		break

print('%i rooms, %i square metre(s) left over' % (num_rm, floor))
