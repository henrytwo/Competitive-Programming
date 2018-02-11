num_ball = int(input())
balls = list(map(int, input().split()))

best = 0

'''
def rec(state):

	global best

	if max(state) > best:
		best = max(state)

	for n in range(0, len(state) - 1):
		v = state[:]
		if v[n] == v[n + 1]:
			v[n] *= 2
			del v[n + 1]
			rec(v)

	for n in range(0, len(state) - 2):
		v = state[:]
		if v[n] == v[n + 2]:
			v[n] *= 2
			v[n] += v[n + 1]
			del v[n + 2]
			del v[n + 1]
			rec(v)
rec(balls)
'''

while True:
	if max(balls) > best:
		best = max(balls)

	action = False

	for n in range(0, len(balls) - 1):
		if n + 1 < len(balls) and balls[n] == balls[n + 1]:
			balls[n] *= 2
			del balls[n + 1]
			action = True

	for n in range(0, len(balls) - 2):
		if n + 2 < len(balls) and  balls[n] == balls[n + 2]:
			balls[n] *= 2
			balls[n] += balls[n + 1]
			del balls[n + 2]
			del balls[n + 1]
			action = True

	if not action:
		break

print(best)
