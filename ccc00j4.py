import sys
input = sys.stdin.readline

init_streams = int(input())
flows = []

for _ in range(init_streams):
	flows.append(int(input()))

while True:

	i = int(input())

	if i == 77:
		break
	elif i == 88:
		# join
		num_join = int(input()) - 1

		flows[num_join] += flows[num_join + 1]
		del flows[num_join + 1]

	elif i == 99:
		# split

		num_split = int(input()) - 1
		percent_left = int(input())

		left = flows[num_split] * percent_left / 100

		flows[num_split] -= left
		flows.insert(num_split, left)

print(' '.join([str(int(i)) for i in flows]))

# 10 20 30
# 5 5 20 30
# 5 5 50
# 5 55
