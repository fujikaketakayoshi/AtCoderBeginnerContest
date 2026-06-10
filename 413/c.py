import sys
input = sys.stdin.readline
from collections import deque


Q = int(input())

q = deque()
for _ in range(Q):
  query = list(map(int, input().split()))
  # print(query)
  if query[0] == 1:
    c, x = query[1], query[2]
    q.append((x, c))
  else:
    k = query[1]
    ans = 0
    while q:
      x, c = q.popleft()
      if c >= k:
        c -= k
        if c > 0:
          q.appendleft((x, c))
        ans += x * k
        print(ans)
        break
      else:
        k -= c
        ans += x * c
