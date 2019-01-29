import math
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = 0

def is_sqrt(n):
	return math.ceil(n ** (1/2)) ** 2 == n

def is_cube(n):
	return math.ceil(n ** (1/3)) ** 3 == n

for i in range(a, b + 1):

	if is_sqrt(i) and is_cube(i):
		c += 1

print(c)
