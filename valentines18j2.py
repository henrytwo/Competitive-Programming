import sys
input = sys.stdin.readline

target = int(input())
init, down = list(map(int, input().split()))

claps = 0
count = 0

while True:
	count += 1

	claps += init
	init -= down

	if init <= 0 and 2 * claps < target:
		print('RIP')
		break

	if 2 * claps >= target:
		print(count)
		break
