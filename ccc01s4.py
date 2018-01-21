#ccc01s4.py

num = int(input())

meh = []

xl = []
yl = []

for _ in range(num):
	i = input().split()
	x = int(i[0])
	y = int(i[1])

	xl.append(x)
	yl.append(y)

	meh.append([x, y])

x_cen = (max(xl) - min(xl)) / 2
y_cen = (max(yl) - min(yl)) / 2

#x_cen = 0
#y_cen = 0

top_dist = 0

def dist(x, y):
	global x_cen, y_cen
	return ((x - x_cen) ** 2 + (y - y_cen) ** 2) ** 0.5

for element in meh:
	e = dist(*element)

	if e > top_dist:
		top_dist = e

print(round(top_dist * 2, 200))
