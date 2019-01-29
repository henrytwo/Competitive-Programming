import sys
input = sys.stdin.readline

num = int(input())
state = 'Cuteness by definition is similarity to Carol'
for _ in range(num):
	val = int(input())

	if 10 >= val / 1000 > 1 and state == 'Cuteness by definition is similarity to Carol':
		state = 'Cuteness by definition is similarity to Cactus'

	elif val / 1000 > 10:
		state = 'Something is wrong with these cuteness values'
		break

print(state)
