import sys
input = sys.stdin.readline

num_cact, gg_man = list(map(int, input().split()))

def is_pal(num):
	arr = []

	while num:
		arr.append(num % 10)
		num = num // 10

	if len(arr) % 2 == 0:
		return arr[:len(arr)//2] == arr[len(arr)//2:][::-1]
	else:
		return arr[:len(arr)//2] == arr[len(arr)//2 + 1:][::-1]

optimal_val = (num_cact + gg_man) // 2
dist = -1

while True:
	dist += 1

	top = optimal_val + dist
	bot = optimal_val - dist

	if is_pal(top):
		print(top)
		break

	if is_pal(bot):
		print(bot)
		break
