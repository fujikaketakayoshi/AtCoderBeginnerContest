import sys
from collections import deque

input = sys.stdin.readline

Rt, Ct, Ra, Ca = map(int, input().split())
N, M, L = map(int, input().split())

DIR = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

S = deque()
for _ in range(M):
    d, a = input().split()
    S.append((d, int(a)))

T = deque()
for _ in range(L):
    d, b = input().split()
    T.append((d, int(b)))

# 差分（高橋 - 青木）
dr = Rt - Ra
dc = Ct - Ca

ans = 0

sd, sr = S.popleft()
td, tr = T.popleft()

while True:
    n = min(sr, tr)

    sr -= n
    tr -= n

    vr = DIR[sd][0] - DIR[td][0]
    vc = DIR[sd][1] - DIR[td][1]

    # n回の中で k回後に一致するか（1<=k<=n）
    if vr == 0 and vc == 0:
        if dr == 0 and dc == 0:
            ans += n

    elif vr == 0:
        if dr == 0 and vc != 0:
            if (-dc) % vc == 0:
                k = (-dc) // vc
                if 1 <= k <= n:
                    ans += 1

    elif vc == 0:
        if dc == 0 and vr != 0:
            if (-dr) % vr == 0:
                k = (-dr) // vr
                if 1 <= k <= n:
                    ans += 1

    else:
        if (-dr) % vr == 0 and (-dc) % vc == 0:
            kr = (-dr) // vr
            kc = (-dc) // vc
            if kr == kc and 1 <= kr <= n:
                ans += 1

    # 区間終了後の差分更新
    dr += vr * n
    dc += vc * n

    if sr == 0:
        if not S:
            break
        sd, sr = S.popleft()

    if tr == 0:
        if not T:
            break
        td, tr = T.popleft()

print(ans)