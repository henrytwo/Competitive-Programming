import sys
input = sys.stdin.readline

num_gift = int(input())
gifts = list(map(int, input().split()))

done = sorted(gifts)[::-1]
operations = 0

while gifts != done:
	
	for x in range(len(gifts) - 1):

		if gifts[x] < gifts[x + 1]:
			operations += 1
			buffer = gifts[x]
			gifts[x] = gifts[x + 1]
			gifts[x + 1] = buffer

print(operations)
