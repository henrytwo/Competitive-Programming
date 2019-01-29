l = int(input())

def exp(target, h):

	global hops

	if target in g:
		for e in g[target]:
			exp(e, h + 1)
	else:
		if h > hops:
			hops = h

for list_num in range(l):
	n = int(input())
	names = []
	g = {}

	hops = 0

	for n_num in range(n):
		names.append(input())

	root = names[-1]
	s = [names[-1]]

	for name in names:
		if name not in s:
			if s[-1] in g:
				g[s[-1]].append(name)
			else:
				g[s[-1]] = [name]

		if name not in s:
			s.append(name)
		else:
			del s[-1]

	exp(root, 0)

	print((n - hops * 2) * 10)
