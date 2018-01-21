import math

num_x = int(input())
num_y = int(input())
num_shops = int(input())

arr = [[0 for __ in range(num_y)] for _ in range(num_x)]

for _ in range(num_shops):
	x_pos, y_pos, rg, bitrate = [int(i) for i in input().split()]

	x_pos -= 1
	y_pos -= 1

	for x in range(-1 * rg, rg + 1):
		y_ = math.floor((rg ** 2 - x ** 2) ** 0.5)

		y_tarA = y_ + y_pos
		y_tarB = y_ * -1 + y_pos + 1

		x_tar = x + x_pos

		x_tar = max(0, x_tar)
		y_tarA = max(0, y_tarA)

		if x_tar < num_x:
			print(x_tar, y_tarA, bitrate)
			print(x_tar, y_tarB, -1 * bitrate)

			arr[x_tar][y_tarA] += bitrate

			if 0 <= y_tarB < num_y:
				arr[x_tar][y_tarB] += -1 * bitrate

for line in arr[::-1]:
        print(line)

for a in range(len(arr)):
	for b in range(1, len(arr[a])):
		arr[a][b] += arr[a][b - 1]

for line in arr[::-1]:
	print(line)
