#!/bin/python
# ccc02s4.py

import pprint
import sys

input = sys.stdin.readline

max_humans = int(input().strip())

humans = []

for _ in range(int(input())):
	name = input().strip()
	speed = int(input().strip())

	humans.append([[name, speed]])

current_best_time = 9999
current_best = [[] for _ in range(100)]

def lol(depth, current, left, current_time):
	global max_humans, current_best, current_best_time

	print(depth, current, left, current_time)

	if len(left) > 0: # and depth + 1 < len(current_best): # Still has stuff left

		#lol(depth + 1, current + [left[0]], left[1:])

		if len(current) > 0 and len(current[-1]) < max_humans: # Existing branch
			current_clone = current[:][:]
			current_clone[-1] += left[0]

			if left[0][0][1] > current_clone[-1][0][1]:
				offset = left[0][0][1] - current_clone[-1][0][1]
			else:
				offset = 0

			lol(depth, current_clone, left[1:], current_time + offset)


		# New branch
		lol(depth + 1, current + [left[0]], left[1:], current_time + left[0][0][1])

	else:
		#print('nope', depth, current_best)

		if depth < len(current_best) and current_time < current_best_time:
			current_best = current
			current_best_time = current_time

lol(0, [], humans, 0)
import pprint
pprint.pprint(current_best)

#print(humans)
