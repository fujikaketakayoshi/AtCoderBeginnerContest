import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
# print(N, M)

degrees = [0] * N

for _ in range(M):
  A, B = map(int, input().split())
  # print(A, B)
  A -= 1
  B -= 1
  degrees[A] += 1
  degrees[B] += 1
# print(degrees)

hq = []
for d in degrees:
  heapq.heappush(hq, -d)

ans = 0
while hq[0] < -2:
  x = heapq.heappop(hq)
  y = heapq.heappop(hq)
  # print(x, y)
  x += 1
  y += 1
  heapq.heappush(hq, x)
  heapq.heappush(hq, y)
  ans += 1

# hq2 = [-x for x in hq]
# print(hq2)

# while hq2[0] < 2:
#   x = heapq.heappop(hq2)
#   y = heapq.heappop(hq2)
#   x += 1
#   y += 1
#   heapq.heappush(hq2, x)
#   heapq.heappush(hq2, y)
#   ans += 1

hq2 = [-d for d in hq]
# print(hq2)

cnt0 = 0
cnt1 = 0
for d in hq2:
  if d == 0:
    cnt0 += 1
  elif d == 1:
    cnt1 += 1

if cnt0 == 1 and cnt1 == 0:
  ans += 3
elif cnt0 >= 2:
  ans += cnt0

if cnt1 % 2 == 0:
  ans += cnt1 // 2
print(ans)