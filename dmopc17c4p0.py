import sys
input = sys.stdin.readline

points = []

for _ in range(3):
	points.append([int(i) for i in input().split()])

def dist(a, b):
	return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

min_dist = 10 ** 10

for a in range(3):
	for b in range(a):
		d = dist(points[a], points[b])

		if d < min_dist:
			min_dist = d

print(int(d) ** 2)
