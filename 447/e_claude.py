import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.components = n  # 連結成分数を管理
    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.components -= 1  # 成分数を1減らす
        return True

MOD = 998244353

N, M = map(int, input().split())
uvs = []
for _ in range(M):
    U, V = map(int, input().split())
    uvs.append((U - 1, V - 1))

uf = UnionFind(N)
keep_sum = 0

for i in range(M - 1, -1, -1):
    u, v = uvs[i]
    ru, rv = uf.find(u), uf.find(v)
    if ru == rv:
        # 同じ成分内の辺→残してOK
        keep_sum = (keep_sum + pow(2, i + 1, MOD)) % MOD
    else:
        # 異なる成分をつなぐ辺→unionすると成分数が1減る
        if uf.components - 1 >= 2:  # union後も非連結のまま
            uf.union(u, v)
            keep_sum = (keep_sum + pow(2, i + 1, MOD)) % MOD
        # 成分数が2のときはunionすると連結になるので削除

total = 0
for i in range(1, M + 1):
    total = (total + pow(2, i, MOD)) % MOD

ans = (total - keep_sum + MOD) % MOD
print(ans)