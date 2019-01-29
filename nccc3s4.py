n = int(input())
p = []
g = {}

for _ in range(n):
	p.append(int(input()))

for a in range(len(p)):
	g[a] = []
	for b in range(len(p)):
		if a != b:
			g[a].append(b)

print(g)
