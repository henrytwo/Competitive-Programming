#ccc01s4.py

num = int(input())

meh = []

for _ in range(num):
	meh.append([int(i) for i in input().split()])

top_dist = 0

def diameter(a, b, c):
	return (2 * a * b * c) / ((a ** 2 + b ** 2 + c ** 2) ** 2 - (2 * (a ** 4 + b ** 4 + c ** 4))) ** 0.5

def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

for outer in range(len(meh)):
	for inner in range(outer):
		for inner_inner in range(inner):
			a = dist(*meh[outer], *meh[inner])
			b = dist(*meh[inner], *meh[inner_inner])
			c = dist(*meh[inner_inner], *meh[outer])

			print(meh[outer], meh[inner], meh[inner_inner])
			print(a, b, c)

			d = diameter(a, b, c)

			print(d)

			if d > top_dist:
				top_dist = d

print(round(top_dist, 2))
