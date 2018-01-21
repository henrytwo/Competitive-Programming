distance = int(input())
num_clubs = int(input())

clubs = []

for _ in range(num_clubs):
	clubs.append(int(input()))

mem = {}
dp = [9999 for _ in range(distance + 1)]
dp[0] = 0

for d in range(distance):
	for club in clubs:
		if d + club <= distance and dp[d + club] > dp[d] + 1:
			dp[d + club] = dp[d] + 1

if dp[-1] != 9999:
	print('Roberta wins in %i strokes.' % dp[-1])
else:
	print('Roberta acknowledges defeat.')
