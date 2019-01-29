slices = int(input())
fruit = list(map(int, input().split()))

count = 0

for f in fruit:
	for n in range(1, int(f ** 0.5)):
		if f % n == 0:
			break
	else:
		count += 1

print(count)
