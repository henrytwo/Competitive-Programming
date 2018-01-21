p, f = [int(i) for i in input().split()]
costs = list(map(int, input().split()))

cost = 0

for person in range(f):
	q = []

	for plant in costs:
		
