#ccc08s3
import queue

num_cases = int(input())

for case in range(num_cases):
	width = int(input())
	height = int(input())

	grid = []

	for h in range(width):
		grid.append(list(input()))

	solved = set()
	q = queue.Queue()

	q.put((0, 0, 1))

	broken = False

	while not q.empty():
		x, y, c = q.get()
		solved.add((x, y))

		char  = grid[x][y]

		if x == width - 1 and y == height - 1:
			print(c)
			broken = True
			break

		if char == '-' or char == '+':
			if y - 1 > -1 and grid[x][y - 1] != '*':
				if (x, y - 1) not in solved:
					q.put((x, y - 1, c + 1))

			if y + 1 < height and grid[x][y + 1] != '*':
				if (x, y + 1) not in solved:
					q.put((x, y + 1, c + 1))

		if char == '|' or char == '+':
			if x - 1 > -1 and grid[x - 1][y] != '*':
				if (x - 1, y) not in solved:
					q.put((x - 1, y, c + 1))

			if x + 1 < width and grid[x + 1][y] != '*':
				if (x + 1, y) not in solved:
					q.put((x + 1, y, c + 1))

	if not broken:
			print(-1)
