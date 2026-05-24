import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

# ① mod K にする
B = [a % K for a in A]
maxA = max(A)
for i in range(N - 1):
  shou = (maxA - A[i]) // K
  A[i] += shou * K
print(A, B)


# ② ソート
A.sort()

# ③ dequeに入れる
q = deque(A)

# ④ 初期値
ans = q[-1] - q[0]

# ⑤ N回操作
for _ in range(N):
    x = q.popleft()
    q.append(x + K)
    ans = min(ans, q[-1] - q[0])

print(ans)