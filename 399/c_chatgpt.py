import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
# print(N, M)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
    
    def same(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(N + 1)

ans = 0
for _ in range(M):
  u, v = map(int, input().split())
  
  if uf.same(u, v):
    ans += 1
  else:
    uf.union(u, v)

print(ans)