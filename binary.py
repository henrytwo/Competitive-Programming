import sys

input = sys.stdin.readline

def pad(meh):
	if len(meh) % 4 != 0:
		pad = '0' * (4 - len(meh) % 4)
	else:
		pad = ''

	meh = pad + meh

	print(meh)

	if len(meh) > 4:
		for i in range(len(meh), 3, -4):
			meh = meh[:i] + " " + meh[i:]

	return meh

num_pineapple = int(input())
for pineapple in range(num_pineapple):
	n = int(input())

	if n == 0:
		print('0000')
	else:
		print(pad(bin(n)[2:]))
