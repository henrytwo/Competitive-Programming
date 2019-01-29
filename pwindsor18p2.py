import sys
input = sys.stdin.readline

numbagoose = int(input())

point = (0, 0)
dist = -1

for _ in range(numbagoose):
	x, y = [int(i) for i in input().split()]

	if (x ** 2 + y ** 2) ** 0.5 > dist:
		dist = (x ** 2 + y ** 2) ** 0.5
		point = (x, y)


print(point[0], point[1])
