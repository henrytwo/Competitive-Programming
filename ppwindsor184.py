import sys
input = sys.stdin.readline

numempty, numhate = [int(i) for i in input().strip().split()]

#street = [-1 for _ in range(1000)]
empty = []
hate = []

best_house = -1
best_dist = -1

for _ in range(numempty):
	empty.append(int(input()))

	#street[int(input())] = 0

for _ in range(numhate):
	hate.append(int(input()))

	#street[int(input())] = 1

#print(street)

#print(empty)

for house in sorted(empty)[::-1]:
	closest = 999999

	for h in hate:
		if abs(house - h) < closest:
			closest = abs(house - h)

	#empty[house] = closest

	if closest >= best_dist:
		best_dist = closest
		best_house = house

print(best_house)

