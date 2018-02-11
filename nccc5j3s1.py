import sys

input = sys.stdin.readline

num_cact, median = [int(i) for i in input().split()]
cact = [int(i) for i in input().split()]
beep = set()
gud = 0

def med(l):
	if len(l) == 1:
		return cact[l[0]]
	elif len(l) == 2:
		return sum(cact[l[0]], cact[l[1]]) / 2
	else:
		return sorted([cact[l[0]], cact[l[1]], cact[l[2]]])[1]

def sheep(left, done):

	global gud

	if len(done) == 3 or len(done) == num_cact:
		m = med(done)

		if m == median:
			gud += 1

	else:
		for char in left:
			d = done[:]
			d.append(char)
			l = left[:]
			del l[l.index(char)]

			meh = tuple(set(d))

			if meh not in beep:
				sheep(l, d)
				beep.add(meh)

sheep([i for i in range(len(cact))], [])

print(gud)
