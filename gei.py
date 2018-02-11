import sys
input = sys.stdin.readline

l, c = [int(i) for i in input().split()]
bad = []
mir = []

for _ in range(c):
	bad.append(int(input()))


print(int(((c - 2) * (c - 1))/2))
