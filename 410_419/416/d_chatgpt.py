import sys
input = sys.stdin.readline

from bisect import bisect_left

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
        # [0, i)
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l)

    def lower_bound(self, w):
        """
        sum(idx) >= w となる最小 idx を返す
        """
        if w <= 0:
            return 0

        x = 0
        k = 1 << (self.n.bit_length() - 1)

        while k:
            if x + k <= self.n and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k >>= 1

        return x


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))

    # BIT初期化
    bit = BIT(N)

    for i in range(N):
        bit.add(i, 1)

    success = 0

    for b in B:
        need = M - b

        # need以上の最初の位置
        idx = bisect_left(A, need)

        # idx以降に未使用要素があるか
        remain = bit.range_sum(idx, N)

        if remain > 0:
            # idx以前の個数
            s = bit.sum(idx)

            # (s+1)番目の未使用要素
            use_idx = bit.lower_bound(s + 1)

            success += 1
        else:
            # 最小の未使用要素を使う
            use_idx = bit.lower_bound(1)

        # 使用済みにする
        bit.add(use_idx, -1)

    ans = sum(A) + sum(B) - success * M

    print(ans)

