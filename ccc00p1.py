import sys
import queue

input = sys.stdin.readline

sub_sets = {}
raw_stuff = {}

n = int(input())
sets_end = set()
sets_head = set()

for _ in range(n):
	line = input().strip().split()

	if line[0] not in sub_sets:
		sub_sets[line[0]] = [line[2]]
	else:
		sub_sets[line[0]].append(line[2])

	if line[2].isupper():
		sets_end.add(line[2])

	sets_head.add(line[0])

for i in sets_end - sets_head:
	sub_sets[i] = []

while True:
	all_gud = True

	for k in sub_sets:

		meh_gud = True

		kill = []

		for d in range(len(sub_sets[k])):
			i = sub_sets[k][d]

			if i.isupper() and i not in raw_stuff:
				meh_gud = False
				all_gud = False
			elif i in raw_stuff:
				kill.append(i)
				sub_sets[k] += raw_stuff[i]

		for z in range(len(sub_sets[k]) - 1, -1, -1):
			if sub_sets[k][z] in kill:
				del sub_sets[k][z]

		if meh_gud:
			raw_stuff[k] = sub_sets[k]

	if all_gud:
		break

	print(sub_sets)

#print(raw_stuff)

print(sub_sets)
