import sys
input = sys.stdin.readline

l, c = list(map(int, input().split()))
bad = []
mir = []

for _ in range(c):
	bad.append(int(input()))

for m in range(1, l + 1):
	if m in bad:
		mir.append('C')
	else:
		mir.append('X')

meh = 0

for sublen in range(1, l + 1):
	for i in range(l - sublen + 1):
		if mir[i:i + sublen].count('C') >= 3:
			meh += 1

print(meh)
