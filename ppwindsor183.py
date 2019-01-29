import sys
input = sys.stdin.readline

lines = int(input())

rows = [{'y', 'q', 't', 'w', 'e', 'o', 'p', 'u', 'r', 'i'}, {'s', 'g', 'j', 'k', 'd', 'a', 'h', 'f', 'l'}, {'z', 'c', 'n', 'm', 'v', 'b', 'x'}]

count = 0

for _ in range(lines):
	word = input().strip()

	found = False

	for row in rows:
		for c in word:
			if c not in row:
				break
		else:
			found = True
			break

	if found:
		count += 1

print(count)
