import sys
input = sys.stdin.readline

n = int(input())

grid = [[int(i) for i in input().strip().split()] for _ in range(n)]

for i in range(n):
	
	if list(range(i * n + 1, i * n + n + 1)) != grid[i]:

		s = list(range(i * n + 1, i * n + n + 1))
		a = grid[i]

		diff = 0

		for z in range(n):
			#print(z, s[z], a[z])
			diff += 1 if s[z] != a[z] else 0

		print(diff)
		break

#print(grid)
