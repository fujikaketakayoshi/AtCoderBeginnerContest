import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

# ---- prefix sum ----
P = [0] * (N + 1)
for i in range(N):
    if S[i] == 'A':
        P[i+1] = P[i] + 1
    elif S[i] == 'B':
        P[i+1] = P[i] - 1
    else:
        P[i+1] = P[i]

# ---- 座標圧縮 ----
vals = sorted(set(P))
comp = {v: i for i, v in enumerate(vals)}

# ---- Fenwick Tree ----
size = len(vals)
bit = [0] * (size + 1)

def add(i, x):
    i += 1
    while i <= size:
        bit[i] += x
        i += i & -i

def sum_(i):
    s = 0
    i += 1
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

# ---- main ----
ans = 0
for x in P:
    idx = comp[x]
    ans += sum_(idx - 1)  # 自分より小さいもの
    add(idx, 1)

print(ans)
