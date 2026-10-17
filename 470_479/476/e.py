import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = list(map(int, input().split()))
print(N, M)
print(P)

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    # i以下の最大値
    def querymax(self, l, r):
        res = None
        id = None
        while r > l:
            if res:
              if res < self.bit[r]:
                res = self.bit[r]
                id = r
            else:
              res = self.bit[r]
              id = r
            res = max(res, self.bit[r])
            r -= r & -r
        return id

    def querymin(self, l, r):
        res = None
        id = None
        while r > l:
            if res:
              if res > self.bit[r]:
                res = self.bit[r]
                id = r
            else:
              res = self.bit[r]
              id = r
            r -= r & -r
        return id

    # iの位置にvalueを反映
    def update(self, i, value):
        while i <= self.n:
            self.bit[i] = value
            i += i & -i


bit = Fenwick(N)
for i, p in enumerate(P):
  bit.update(i + 1, p)

for _ in range(M):
  L, R = map(int, input().split())
  print(L, R)
  maxid = bit.querymax(L, R)
  minid = bit.querymin(L, R)
  print(maxid, minid)
  bit.update(maxid, P[minid - 1])
  bit.update(minid, P[maxid - 1])
  P[maxid - 1], P[minid - 1] = P[minid - 1], P[maxid - 1]
  print(P)
  print(bit.bit)

print(*P)