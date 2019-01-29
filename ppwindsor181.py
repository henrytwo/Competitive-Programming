import sys
input = sys.stdin.readline

thing = int(input())

stuff = 0

for i in range(1, thing + 1):
	if thing % i == 0:
		stuff += i

print(stuff)
