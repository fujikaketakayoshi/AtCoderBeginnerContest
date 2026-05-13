import sys
input = sys.stdin.readline
import heapq

N, Q = map(int, input().split())
# print(N, Q)
PC = list(range(1, N + 1))
# print(PC)
heapq.heapify(PC)

cnt = [0] + [1] * N
# print(cnt)

for _ in range(Q):
  X, Y = map(int, input().split())
  # print(X, Y)
  ans = 0
  while PC[0] <= X:
    x = heapq.heappop(PC)
    ans += cnt[x]
    cnt[Y] += cnt[x]
    cnt[x] = 0
  # print(cnt)
  print(ans)
