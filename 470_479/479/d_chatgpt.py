import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)
INF = 10 ** 20

L = [INF] + list(map(int, input().split()))
R = list(map(int, input().split())) + [INF]
# print(L)
# print(R)

class SegTree:
    def __init__(self, A):
        n = len(A)

        self.size = 1
        while self.size < n:
            self.size *= 2

        self.data = [float("inf")] * (self.size * 2)

        for i in range(n):
            self.data[self.size + i] = A[i]

        for i in range(self.size - 1, 0, -1):
            self.data[i] = min(
                self.data[i * 2],
                self.data[i * 2 + 1]
            )

    def query(self, l, r):
        l += self.size
        r += self.size

        ans = float("inf")

        while l < r:
            if l % 2 == 1:
                ans = min(ans, self.data[l])
                l += 1

            if r % 2 == 1:
                r -= 1
                ans = min(ans, self.data[r])
            l //= 2
            r //= 2
        return ans

segL = SegTree(L)
segR = SegTree(R)

for _ in range(Q):
  s, t = map(int, input().split())
  # print(s, t)
  s -= 1
  t -= 1
  ans = float('inf')
  if s < t:
    # 右に即移動
    ans = min(ans, R[s])
    # 左に行って右へ
    ans = min(ans, L[s] + segR.query(0, s))
  else:
    # 左に即移動
    ans = min(ans, L[s])
    # 右に行って左へ
    ans = min(ans, R[s] + segL.query(s + 1, N))
  print(ans)
