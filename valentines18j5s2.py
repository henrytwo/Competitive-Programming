import sys
import queue
input = sys.stdin.readline

deals = []

num_orchid, num_deals = list(map(int, input().split()))

for _ in range(num_orchid):
	meh = [0 for __ in range(num_orchid)]
	meh[_] = 1

	deals.append([int(input())] + meh)

for _ in range(num_deals):
	deals.append(list(map(int, input().split())))

quantity = list(map(int, input().split()))

best = 10 ** 10

def vsum(a, b):
	for i in range(len(b)):
		a[i] += b[i]
	return a

def vdif(a, b):
	for i in range(len(b)):
		a[i] -= b[i]
		if a[i] < 0:
			return False

	return True

q = queue.Queue()
empty = [0 for _ in range(num_orchid + 1)]

for e in deals:
	q.put((e, empty[:]))

while not q.empty():
	mask, prev = q.get()

	new = vsum(mask, prev)

	#print('Mask',mask,'Prev' , prev, 'New', new, 'len', q.qsize())

	if vdif(quantity[:], new[1:]):
		if new[0] < best and sum(quantity[:]) - sum(new[1:]) == 0:
			best = new[0]

		for d in deals:
			#print(new, vsum(d[1:], new[1:]), vdif(quantity[:],vsum(d[1:], new[1:])))
			#print(new, vsum(d[1:], prev[1:]), vdif(quantity[:],vsum(d[1:], new[1:])))

			if vdif(quantity[:],vsum(d[1:], new[1:])):
				#print(new, vsum(d, new))
				q.put((d[:], new))
				#print('ADDED', new)

			#if vdif(quantity[:],vsum(d[1:], prev[1:])) and prev != empty:
				#print(new, vsum(d, prev))
			#	q.put((d[:], prev[:]))

print(best)
