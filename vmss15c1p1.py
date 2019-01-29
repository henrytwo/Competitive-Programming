import sys
import math
input = sys.stdin.readline

soil = int(input())

w = soil ** 0.5
h = soil ** 0.5

if (int(w) != w and int(h) != h):
	c = 0
	while True:
		c += 1

		if soil / (int(w) + c) == int(soil / (int(w) + c)):
			h = int(soil / (int(w) + c))
			w = int(w + c)
			break

		if soil / (int(w) - c) == int(soil / (int(w) - c)):
			h = int(soil / (int(w) - c))
			w = int(w - c)
			break

print(int(2 * w + 2 * h))
