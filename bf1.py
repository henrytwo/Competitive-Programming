import sys

num_pineapples = int(input())
pineapples = []

for pineapple in range(num_pineapples):
    pineapples.append(int(input()))
    
for val in sorted(pineapples):
    print(val)
