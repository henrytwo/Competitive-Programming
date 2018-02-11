i = list(input())

c = {}

unique = list(set(i))

if len(set(i)) <= 2:
	print(0)
else:
	for char in unique:
		l = i.count(char)
		if l in c:
			c[l].append(char)
		else:
			c[l] = [char]

	master = []
	for e in reversed(sorted(c)):
		master += c[e]

	print(len(i) - i.count(master[0]) - i.count(master[1]))
