import sys
input = sys.stdin.readline

num_blocks = int(input())
blocks = sorted(list(map(int, input().split())))

configs = [set() for _ in range(blocks[-1] + blocks[-2])]
heights = [0 for _ in range(blocks[-1] + blocks[-2])]

for a in range(len(blocks)):
	for b in range(a + 1, len(blocks)):
		if (a, b) not in configs[blocks[a] + blocks[b] - 1]:
			heights[blocks[a] + blocks[b] - 1] += 1
			configs[blocks[a] + blocks[b] - 1].add((a, b))

max_width = max(heights)

print(heights)
print(configs)
print(max_width, heights.count(max(heights)))
