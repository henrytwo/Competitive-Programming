import sys
input = sys.stdin.readline

nodes = {}

while True:
	i = input().strip()

	if i == '**':
		break

	if i[0] in nodes:
		nodes[i[0]].append(i[1])
	else:
		nodes[i[0]] = [i[1]]

	if i[1] in nodes:
		nodes[i[1]].append(i[0])
	else:
		nodes[i[1]] = [1[0]]

print(nodes)
