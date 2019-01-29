import sys

# Honestly, just don't read this code
# The bash is too strong

input = sys.stdin.readline

numbers = [-1 for _ in range(1001)]

for _ in range(int(input())):
	lel = int(input())
	numbers[lel] += 1

mumbers = numbers[:]

thiccest_num = len(numbers) - numbers[::-1].index(max(numbers)) - 1
numbers[thiccest_num] = - 1
smol_num = numbers.index(max(numbers))

ceh = abs(thiccest_num - smol_num)

smol_num = mumbers.index(max(mumbers))
mumbers[smol_num] = -1
thiccest_num = len(mumbers) - mumbers[::-1].index(max(mumbers)) - 1
#mumbers[thiccest_num] = - 1
#smol_num = mumbers.index(max(mumbers))

peh = abs(thiccest_num - smol_num)

print(max(ceh, peh))

