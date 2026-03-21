import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.group_count = n # 現在の連結成分の数

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
        self.group_count -= 1
        return True

N, M = map(int, input().split())
uvs = []
for i in range(1, M + 1):
    u, v = map(int, input().split())
    uvs.append((u - 1, v - 1, i))

# 辺のコストが大きい順 (Mから1) に検討
uvs.reverse()

uf = UnionFind(N)
total_keep_cost = 0
MOD = 998244353

for u, v, idx in uvs:
    # この辺を追加しても「連結(成分数1)」にならないか判定
    
    # 1. すでに成分数が1になることはありえない（制約上ないはずですが念のため）
    # 2. まだ成分数が3以上あるなら、どの辺を繋いでも成分数は2以上を維持できる
    if uf.group_count > 2:
        uf.union(u, v)
        total_keep_cost = (total_keep_cost + pow(2, idx, MOD)) % MOD
    
    # 3. 成分数がちょうど2のとき
    elif uf.group_count == 2:
        # 同じグループ内の辺なら追加しても成分数は2のまま！
        if uf.find(u) == uf.find(v):
            total_keep_cost = (total_keep_cost + pow(2, idx, MOD)) % MOD
        # 違うグループを結ぶ辺だと成分数が1になってしまうので、追加しない（スルー）

# (全ての辺の合計コスト) - (残せたコストの最大値) = (削除コストの最小値)
# 全合計コスト S = 2^1 + 2^2 + ... + 2^M = 2^(M+1) - 2
total_all_cost = (pow(2, M + 1, MOD) - 2 + MOD) % MOD
ans = (total_all_cost - total_keep_cost + MOD) % MOD

print(ans)