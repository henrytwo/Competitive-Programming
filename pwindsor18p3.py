import sys
input = sys.stdin.readline

numba = int(input())

count = 0

for _ in range(numba):
	value = int(input())

	prime = True

	#print(value, 'shit')

	if value > 2:
		for r in range(2, int(value ** 0.5) + 1):
			if value % r == 0:
				prime = False

				#print(value, r)

				break

		if not prime:
			count += 1

print(count)
