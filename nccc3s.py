num = int(input())

points = []

sx = []
sy = []

for n in range(num):
	x, y = [int(i) for i in input().split()]
	points.append((x, y))

	sx.append(x)
	sy.append(y)

sy = sum(sy) / len(points)
sx = sum(sx) /  len(points)

def dist(sx, sy, ex, ey):
	return ((sx - ex) ** 2 + (sy - ey) ** 2) ** 0.5

best = 0

for p in points:
	d = dist(p[0], p[1], sx, sy)

	if d > best:
		best = d

	for n in points:
		d = dist(p[0], p[1], n[0], n[1]) / 2
		if d > best:
			best = d

print(best)
