import sys
input = sys.stdin.readline

n = int(input())

t = n * (n - 1)/2
c = 0
kill = False

for k in range(1, n):

	for l in range(k + 1, n + 1):
		c += 1

		if 2 * c >= t:
			print(k)
			kill = True
			break

	if kill:
		break


