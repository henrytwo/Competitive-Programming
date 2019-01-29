import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
	line = input()

	valid = True


	print('yes' if valid else 'no')
