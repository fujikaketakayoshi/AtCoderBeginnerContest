import sys
input = sys.stdin.readline
import heapq

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

Ap = []
Am = []
for a in A:
  if a > 0:
    heapq.heappush(Ap, a)
  else:
    heapq.heappush(Am, -a)

# print(Ap)
# print(Am)

i = 0
ans = 0
while Ap or Am:
  if Ap and Am:
    if Ap[0] - i >= Am[0] + i:
      ans += Am[0] + i
      i = -Am[0]
      heapq.heappop(Am)
    else:
      ans += Ap[0] - i
      i = Ap[0]
      heapq.heappop(Ap)
  elif Ap:
    ans += Ap[0] - i
    i = Ap[0]
    heapq.heappop(Ap)
  else:
    ans += Am[0] + i
    i = -Am[0]
    heapq.heappop(Am)

print(ans)