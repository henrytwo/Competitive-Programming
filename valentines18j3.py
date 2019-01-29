import sys

input = sys.stdin.readline

num_people = int(input())
people = {}
cuteness_scale = [0 for _ in range(10 ** 6)]

for _ in range(num_people):
	i = input().split()
	name = i[0]
	cuteness = int(i[1])

	people[name] = cuteness
	cuteness_scale[cuteness] += 1

for n in people:
	if sum(cuteness_scale[:people[n]]) > num_people // 2:
		print('%s is cute! <3' % n)
	else:
		print('%s is not cute. </3' % n)

