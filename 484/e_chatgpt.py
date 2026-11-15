import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right


class SegmentTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)

    def add(self, i, x):
        i += self.size
        self.tree[i] += x

        while i > 1:
            i //= 2
            self.tree[i] = (
                self.tree[i * 2]
                + self.tree[i * 2 + 1]
            )

    def query(self, l, r):
        # 半開区間 [l, r)
        l += self.size
        r += self.size
        res = 0

        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]

            l //= 2
            r //= 2

        return res


N, L, R = map(int, input().split())
A = list(map(int, input().split()))

# 累積和
S = [0]
for a in A:
    S.append(S[-1] + a)

# 座標圧縮
X = sorted(set(S))
idx = {x: i for i, x in enumerate(X)}

seg = SegmentTree(len(X))

ans = 0

for s in S:
    l = bisect_left(X, s - R)
    r = bisect_right(X, s - L)

    ans += seg.query(l, r)

    seg.add(idx[s], 1)

print(ans)