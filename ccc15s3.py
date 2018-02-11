num_gate = int(input())

num_plane = int(input())

gates = [0 for _ in range(num_gate)]
num_fill = 0
cap = num_gate - 1

for p in range(num_plane):
	num = int(input())

	for g in range(min(num - 1, cap), -1, -1):
		if gates[g] == 0:
			num_fill+=1
			gates[g] = num

			if g == cap - 1:
				cap = g

			break
	else:
		break

print(num_fill)
