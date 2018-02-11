import queue

masks = [[2, 1, 0, 2],
	 [1, 1, 1, 1],
	 [0, 0, 2, 1],
	 [0, 3, 0, 0],
	 [1, 0, 0, 1]]

cases = int(input())

def r(a, b, c, d):
	if [a, b, c, d] in mem:
		return mem[[a, b, c, d]]
	else:
		if a - 2 > -1 and b - 1 > -1 and d - 2 > -1:
			r(a - 2, b - 1, c, d - 2)
                r(a - 1, b - 1, c - 1, d - 1)
                r(a, b, c - 2, d - 1)
                r(a, b - 3, c, d - 0)
                r(a - 1, b, c, d - 1)

for c in range(cases):
	pos = list(map(int, input().split()))

	mem = {}


	'''
	queue_sheit = queue.Queue()
	queue_sheit.put([0, 0, 0, 0])

	while not queue_sheit.empty():
		meh = queue_sheit.get()[:]

		if meh == pos:
			print("Meh")

		for m in masks:
			meh2 = meh[:]

			for i in range(4):
				meh2[i] += m[i]

				if meh2[i] > 30:
					print(meh2)
					break

			else:
				queue_sheit.put(meh2)

	'''
