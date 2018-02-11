lines = int(input())

med = []

for l in range(lines):
	vals = list(map(int, input().split()))
	vals.sort()

	med.append(vals[len(vals) // 2])

print(med[len(med) // 2])
