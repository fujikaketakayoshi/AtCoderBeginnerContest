import sys
input = sys.stdin.readline
from math import gcd
from functools import cmp_to_key

# ---------- 入力 ----------
N, Q = map(int, input().split())

raw_dirs = []
for _ in range(N):
    x, y = map(int, input().split())
    g = gcd(abs(x), abs(y))
    x //= g
    y //= g
    raw_dirs.append((x, y))

queries = []
for _ in range(Q):
    a, b = map(int, input().split())
    queries.append((a - 1, b - 1))

# ---------- 方向ごとにカウント ----------
cnt = {}
for d in raw_dirs:
    cnt[d] = cnt.get(d, 0) + 1

dirs = list(cnt.keys())

# ---------- 偏角ソート用比較 ----------
def half(p):
    x, y = p
    return 0 if (y > 0 or (y == 0 and x > 0)) else 1

def cmp(a, b):
    ha = half(a)
    hb = half(b)
    if ha != hb:
        return ha - hb
    # 外積 a × b
    cross = a[0] * b[1] - a[1] * b[0]
    if cross > 0:
        return -1
    if cross < 0:
        return 1
    return 0

dirs.sort(key=cmp_to_key(cmp))

# ---------- index化 ----------
pos = {}
for i, d in enumerate(dirs):
    pos[d] = i

# ---------- prefix sum ----------
M = len(dirs)
prefix = [0] * (M + 1)
for i in range(M):
    prefix[i + 1] = prefix[i] + cnt[dirs[i]]

# ---------- クエリ処理 ----------
out = []
for a, b in queries:
    da = raw_dirs[a]
    db = raw_dirs[b]
    ia = pos[da]
    ib = pos[db]

    # CCWで B -> A を進む = CWで A -> B
    if ib <= ia:
        ans = prefix[ia + 1] - prefix[ib]
    else:
        ans = (prefix[M] - prefix[ib]) + prefix[ia + 1]

    print(ans)