#ccc01s1.py

line = input()

c = [line[1 : line.index('D')],
     line[1 + line.index('D') : line.index('H')],
     line[1 + line.index('H') : line.index('S')],
     line[1 + line.index('S') :]]

p = [0,0,0,0]

d = {'A' : 4, 'K':3, 'Q':2, 'J':1}

for i in range(len(c)):
	for char in c[i]:
		if char in d:
			p[i] += d[char]
	if len(c[i]) == 0:
		p[i] += 3

	elif len(c[i]) == 1:
		p[i] += 2

	elif len(c[i]) == 2:
		p[i] += 1


print('Cards Dealt              Points')
print('Clubs %-23s %-i' % (' '.join(list(c[0])), p[0]))
print('Diamonds %-20s %-i' % (' '.join(list(c[1])), p[1]))
print('Hearts %-22s %-i' % (' '.join(list(c[2])), p[2]))
print('Spades %-22s %-i' % (' '.join(list(c[3])), p[3]))
print('                       Total %2i' % sum(p))
