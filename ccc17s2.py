import sys
input = sys.stdin.readline

num = int(input())
pineapples = sorted(list(map(int, input().split())))[::-1]

low = pineapples[num // 2:]
high = pineapples[:num // 2][::-1]

new = []

for i in range(num // 2):
	new += [low[i], high[i]]

if num % 2 != 0:
	new.append(low[-1])

print(' '.join(list(map(str, new))))
