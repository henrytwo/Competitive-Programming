import sys
input = sys.stdin.readline

n = int(input())

grid = []

def get_mask(h):
	#return [['#' if x > h - ((2 * y - 1) // 2) and x < h + ((2 * y - 1) // 2) else ' ' for x in range(2 * h - 1)] for y in range(h)]

	meh = []

	for y in range(1, h + 1):
		tiles = 2 * y - 1
		padding = (2 * h - 1 - tiles) // 2

		leh = []

		for x in range(1, 2 * h):
			leh.append('#' if padding < x < 2 * h - padding else ' ')

		meh.append(leh)

	return meh

for _ in range(n):
	grid.append(list(input().split()))

much_gud = 0

for height in range(n):
	mask = get_mask(height + 1)

	#print(mask)

	#for l in mask:
	#	print(l)

	for x in range(n):
		for y in range(n):
			if n - x > len(mask) and n - y > len(mask):
				#print(x, y)

				gud = True

				for sx in range(len(mask)):
					for sy in range(len(mask)):
						try:
							if mask[sy][sx] != grid[y + sy][x + sy] and mask[sy][sx] == '#':
								gud = False
								break
						except:
							pass
					if not gud:
						break

				much_gud += gud

print(much_gud)
#n = get_mask(10)
#for a in n:
#	print(a)
x
