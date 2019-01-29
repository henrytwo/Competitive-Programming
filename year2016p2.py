import sys
input = sys.stdin.readline

days = int(input())

gifts = []

singles = {'1':'st', '2':'nd', '3':'rd'}
bad = ['11', '12', '13']

def pineapple(val):

	if str(val)[-1] in singles:
		if len(str(val)) == 1 or (len(str(val)) > 1 and str(val)[-2:] not in bad):
			return str(val) + singles[str(val)[-1]]
		else:
			return str(val) + 'th'
	else:
		return str(val) + 'th'

for d in range(1, days + 1):
	print('On the %s day of Christmas my true love sent to me:' % pineapple(d))
	gifts.append(input())

	for i in range(len(gifts), 0, -1):
		name  = gifts[i - 1]

		if i == 1 and len(gifts) > 1:
			i = 'and ' + str(i)

		print('%s %s' % (str(i), name))
