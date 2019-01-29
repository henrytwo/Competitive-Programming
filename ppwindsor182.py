import sys
input = sys.stdin.readline

w = int(input())
h = int(input())

for y in range(h):
	buffer = ''

	for x in range(w):
		if y % 2 == 0:
			x += 1

		buffer += '1' if x % 2 == 0 else '0'

	print(buffer)

