import sys
input = sys.stdin.readline

num_jerseys = int(input())
num_athletes = int(input())

jerseys = {}
sizes = ['S', 'M', 'L']
gud = 0

for num in range(num_jerseys):
	jerseys[num + 1] = input().strip('\n')

for _ in range(num_athletes):
	size, num = input().split()

	num = int(num)

	if num in jerseys:
		if sizes.index(jerseys[num]) >= sizes.index(size):
			gud += 1
			del jerseys[num]
print(gud)
