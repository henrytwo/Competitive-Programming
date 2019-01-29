import sys
import math
input = sys.stdin.readline

header = input().strip()
word = input().strip()
filtered = []

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def inc(char, amount):
	i = alpha.index(char)

	return alpha[(i + amount) % 26]

for c in word:
	if c in alpha:
		filtered.append(c)

for c in range(len(header)):
	shift = alpha.index(header[c])

	for i in range(c, len(filtered), len(header)):
		filtered[i] = inc(filtered[i], shift)

print(''.join(filtered))
