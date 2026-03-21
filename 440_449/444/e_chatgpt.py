import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


# ---------- Fenwick Tree ----------
class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        # sum[0..i]
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        if l > r:
            return 0
        return self.sum(r) - (self.sum(l - 1) if l > 0 else 0)


# ---------- input ----------
N, D = map(int, input().split())
A = list(map(int, input().split()))

# ---------- 座標圧縮 ----------
vals = sorted(set(A))
M = len(vals)

# value -> compressed index
comp = {v: i for i, v in enumerate(vals)}

bit = BIT(M)

ans = 0
l = 0

# ---------- two pointers ----------
for r in range(N):
    x = A[r]

    # x と差が D 未満になる値の範囲（実際の値で決める）
    low_val = x - D + 1
    high_val = x + D - 1

    # その値範囲に対応する index 範囲を求める
    left_idx = bisect_left(vals, low_val)
    right_idx = bisect_right(vals, high_val) - 1

    # 条件違反があるなら l を進める
    while left_idx <= right_idx and \
          bit.range_sum(left_idx, right_idx) > 0:
        bit.add(comp[A[l]], -1)
        l += 1

    # A[r] を区間に追加
    bit.add(comp[x], 1)

    # 今回追加できた区間数
    ans += (r - l + 1)

print(ans)
