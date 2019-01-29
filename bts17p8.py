import sys
input = sys.stdin.readline

num = int(input())
pineapple = list(input())

prev = '0'
sum = 0
for i in range(num):
	c = pineapple[i]

	if c == '-':
		prev = prev[:-1]
	else:
		prev += c

	sum += int(prev)

print(sum)
