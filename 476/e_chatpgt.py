import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = list(map(int, input().split()))


class SegTree:
    def __init__(self, A, op, e):
        self.op = op
        self.e = e

        self.size = 1
        while self.size < len(A):
            self.size *= 2

        self.data = [e] * (self.size * 2)

        # 葉
        for i, value in enumerate(A):
            self.data[self.size + i] = value

        # 親を構築
        for i in range(self.size - 1, 0, -1):
            self.data[i] = self.op(
                self.data[i * 2],
                self.data[i * 2 + 1]
            )

    def update(self, i, value):
        i += self.size
        self.data[i] = value

        while i > 1:
            i //= 2
            self.data[i] = self.op(
                self.data[i * 2],
                self.data[i * 2 + 1]
            )

    # [l, r)
    def query(self, l, r):
        l += self.size
        r += self.size

        left_res = self.e
        right_res = self.e

        while l < r:
            if l % 2 == 1:
                left_res = self.op(left_res, self.data[l])
                l += 1

            if r % 2 == 1:
                r -= 1
                right_res = self.op(self.data[r], right_res)

            l //= 2
            r //= 2

        return self.op(left_res, right_res)


# (値, index) を持たせる
A = [(P[i], i) for i in range(N)]

max_seg = SegTree(
    A,
    max,
    (float("-inf"), -1)
)

min_seg = SegTree(
    A,
    min,
    (float("inf"), N)
)


for _ in range(M):
    L, R = map(int, input().split())

    # 入力は1-indexed、SegTreeは0-indexed
    L -= 1

    max_value, max_i = max_seg.query(L, R)
    min_value, min_i = min_seg.query(L, R)

    # swap
    P[max_i], P[min_i] = P[min_i], P[max_i]

    # 変更された2点を両方のSegTreeに反映
    max_seg.update(max_i, (P[max_i], max_i))
    max_seg.update(min_i, (P[min_i], min_i))

    min_seg.update(max_i, (P[max_i], max_i))
    min_seg.update(min_i, (P[min_i], min_i))


print(*P)