#ccc08s3

num_cases = int(input())

for case in range(num_cases):
	width = int(input())
	height = int(input())

	grid = []

	for h in range(width):
		grid.append(list(input()))

	solved = set()
	queue = [(0, 0)]
	graph = {}

	def add_(thing):
		global queue

		if thing not in solved:
			queue.append(thing)

	print("CASE "+ str(case) + "\n")

	while queue:
		x, y = queue[0]
		solved.add(queue[0])
		del queue[0]

		char  = grid[x][y]
		graph[(x, y)] = set()

		if x == width - 1 and y == height - 1:
			print("Done")
			break

		if char == '|' or char == '+':
			if y - 1 > -1 and grid[x][y - 1] != '*':
				graph[(x, y)].add((x, y - 1))
				add_((x, y - 1))

				print("UP")

			if y + 1 < height and grid[x][y + 1] != '*':
				graph[(x, y)].add((x, y + 1))
				add_((x, y + 1))

				print("DOWN")

		if char == '-' or char == '+':
			if x - 1 > -1 and grid[x - 1][y] != '*':
				graph[(x, y)].add((x - 1, y))
				add_((x - 1, y))

				print("LEFT")

			if x + 1 < width and grid[x + 1][y] != '*':
				graph[(x, y)].add((x + 1, y))
				add_((x + 1, y))

				print("RIGHT")

	print(graph)
