import queue

pages = int(input())

graph = {}

for p in range(pages):
	root = input()

	buffer = []

	while True:
		l = input()

		if l == '</HTML>':
			break

		while '<A HREF=' in l:
			url = l[l.index('<A HREF=') + 9: l.index('<A HREF=') + l[l.index('<A HREF='):].index('">')]

			print('Link from %s to %s' % (root, url))
			buffer.append(url)

			l = l[l.index('<A HREF=') + l[l.index('<A HREF='):].index('">') + 2:]

	if root in graph:
		graph[root] += buffer[:]
	else:
		graph[root] = buffer[:]

prev = ''

while True:
	path = input()
	if path == 'The End':
		break

	if not prev:
		prev = path
	else:
		q = queue.Queue()
		q.put(prev)

		solved = False
		meh = []

		while not q.empty():
			i = q.get()

			if path == i:
				print('Can surf from %s to %s.' % (prev, path))
				solved = True
				break
			for e in graph[i]:
				if e not in meh:
					q.put(e)
					meh.append(e)

		if not solved:
			print('Can\'t surf from %s to %s.' % (prev, path))

		prev = ''
