import math
import pprint

start = int(input())
end = int(input())

diff = end - start

chain = [i for i in range(start, end + 1)]

print(chain)

matrix = [[0 for __ in range(math.ceil(diff ** 0.5))] for _ in range(int(diff ** 0.5))]

start = ((len(matrix) - 1) // 2, (len(matrix[0]) - 1) // 2)

print(start)
pprint.pprint(matrix)
