import sys
input = sys.stdin.readline

n = int(input())

s = 0
for _ in range(n):
	s += int(input())

print('%0.1f' % (s / n))
