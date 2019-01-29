import sys
import queue

input = sys.stdin.readline

w = int(input())
h = int(input())

thing = []
start = None

rooms = []
num_rooms = 0

visited = set()

for _ in range(h):
	thing.append(list(input().strip()))

	for i in thing[-1]:
		if i != 'O' and i != '#':
			num_rooms += 1

	if '1' in thing[-1]:
		start = (_, thing[-1].index('1'))


q = queue.Queue()
q.put(start)
#rooms.append(1)

positions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while not q.empty():

	#print(len(rooms), num_rooms)

	if num_rooms <= len(rooms):
		break

	x, y = q.get()

	for p in positions:
		nx, ny = x + p[0], y + p[1]

		if (nx, ny) not in visited and 0 <= ny < len(thing[0]) and 0 <= nx < len(thing) and not thing[nx][ny] == '#':

			q.put((nx, ny))
			visited.add((nx, ny))

			if thing[nx][ny] != 'O':
				rooms.append(thing[nx][ny])

if not rooms:
    rooms.append('1')

print(' '.join(sorted(rooms)))
