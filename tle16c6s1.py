# tle16c6s1.py
# Henry Tu

import sys

pref = []

for _ in range(int(sys.stdin.readline().strip('\n'))):
    pref.append(sys.stdin.readline().strip('\n'))

prob = []

for _ in range(int(sys.stdin.readline().strip('\n'))):
    prob.append(sys.stdin.readline().strip('\n'))

for p in pref:
    while p in prob:
        sys.stdout.write(str(prob.index(p) + 1) + '\n')
        prob[prob.index(p)] = 0
