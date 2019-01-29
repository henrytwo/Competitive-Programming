import sys
input = sys.stdin.readline

num_village = int(input())

villages = []
mids = []
min_diff = 999999999999

for _ in range(num_village):
    villages.append(int(input()))

villages.sort()

for vill in range(len(villages) - 1):
    mids.append((villages[vill] + villages[vill + 1]) / 2)

    if len(mids) > 1:
        if abs(mids[-1] - mids[-2]) < min_diff:
            min_diff = abs(mids[-1] - mids[-2])

#print(villages)
#print(mids)
print("%0.1f" % min_diff)
