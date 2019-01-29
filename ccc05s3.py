import sys
input = sys.stdin.readline

num_arr = int(input())
arrs = []

for _ in range(num_arr):
    temp = []
    h, w = [int(i) for i in input().split()]

    for __ in range(h):
        temp.append([int(i) for i in input().split()])

    arrs.append(temp)

def mult(a, b):
    h1, w1 = len(a), len(a[0])
    h2, w2 = len(b), len(b[0])

    th = h1 * h2
    tw = w1 * w2

    out = []

    for y in range(th):
        out.append([])
        for x in range(tw):

            out[y].append(a[y // h2][x // w2] * b[y % h2][x % w2])

    return out

while len(arrs) > 1:

    arrs[0] = mult(arrs[0], arrs[1])
    del arrs[1]

top_col_sum = 0
bot_col_sum = 10 ** 10
top_row_sum = 0
bot_row_sum = 10 ** 10
top_val = 0
bot_val = 10**10

for line in arrs[0]:
    if top_val < max(line):
        top_val = max(line)

    if bot_val > min(line):
        bot_val = min(line)

    if top_row_sum < sum(line):
        top_row_sum = sum(line)

    if bot_row_sum > sum(line):
        bot_row_sum = sum(line)

for x in range(len(arrs[0])):

    line = []

    for y in range(len(arrs[0][x])):
        line.append(arrs[0][x][y])

    if top_col_sum < sum(line):
        top_col_sum = sum(line)

    if bot_col_sum > sum(line):
        bot_col_sum = sum(line)

print(top_val, bot_val, top_row_sum, bot_row_sum, top_col_sum, bot_col_sum, sep='\n')
