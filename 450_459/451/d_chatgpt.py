import sys
input = sys.stdin.readline

import heapq

N = int(input())
MAX = 10 ** 9

# 2の冪
beki = []
x = 1
while x <= MAX:
    beki.append(x)
    x *= 2

hq = []

# 初期投入
for b in beki:
    heapq.heappush(hq, b)

seen = set(beki)

cnt = 0

while True:
    x = heapq.heappop(hq)
    cnt += 1
    
    if cnt == N:
        print(x)
        break
    
    for b in beki:
        v = int(str(x) + str(b))
        if v > MAX:
            continue
        if v in seen:
            continue
        seen.add(v)
        heapq.heappush(hq, v)