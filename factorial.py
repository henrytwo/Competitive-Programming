import sys
import math
input = sys.stdin.readline

case = int(input())
for _ in range(case):
    print(math.factorial(int(input())) % 2**32)

