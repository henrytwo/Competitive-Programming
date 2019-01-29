h, m, s = [int(x) for x in input().split()]

time = 43200 - (s + 60*m + 3600*h) % 43200

hr = time // 3600
time = time % 3600

mn = time // 60
time = time % 60

sn = time % 60

print('%02i:%02i:%02i' % (hr, mn, sn))
