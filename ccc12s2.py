import sys
input = sys.stdin.readline

meh = input()
out = 0

dicc = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

for i in range(0, len(meh) - 1, 2):

	num = int(meh[i])
	val = dicc[meh[i + 1]]
	mod = 1

	if i + 3 < len(meh):
		if dicc[meh[i + 3]] > val:
			mod = -1

	out += val * num * mod

print(out)
