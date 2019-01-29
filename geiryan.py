from functools import *
import sys

input = sys.stdin.readline

@lru_cache(maxsize=None)
def fac(num):
    if num == 1:
        return 1
    else:
        return num * fac(num-1)
        
for i in range(int(input())):
    print(fac(int(input())) % 2**32)
