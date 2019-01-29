import sys
input = sys.stdin.readline

weight = int(input())
count = 0

pineapple = [1 for _ in range(weight)]

def combine(meh):
    new = []
    for i in range(0, len(meh), 2):
        if len(meh) - i > 1:
            new.append(meh[0] + meh[1])
    return new

while pineapple:
    count += 1
    pineapple = combine(pineapple)
    print(pineapple)

print(combine(pineapple))
print(count)
