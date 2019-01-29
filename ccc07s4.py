points = int(input())
p = []

while True:
    s, e = [int(i) for i in input().split()]
    
    if s == 0 and e == 0:
        break
    
    p.append([s, e])

p.sort()

print(p)

dp = [0 for _ in range(points)]

dp[0] = 1

for s, e in p:
    dp[e - 1] += dp[s - 1]
    
print(dp)
