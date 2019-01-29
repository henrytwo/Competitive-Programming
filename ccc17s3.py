import sys
input = sys.stdin.readline

num_blocks = int(input())
blocks = sorted(list(map(int, input().split())))

configs = []
heights = [0 for _ in range(blocks[-1] + blocks[-2])]

for a in range(len(blocks)):
	for b in range(a + 1, len(blocks)):
		if (blocks[a], blocks[b]) not in configs:
			heights[blocks[a] + blocks[b] - 1] += 1
			configs.append((blocks[a], blocks[b]))

max_width = max(heights)

print(max_width, heights.count(max(heights)))
