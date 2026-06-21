import sys
input = sys.stdin.readline

N, K = map(int, input().split())

LR = [tuple(map(int, input().split())) for _ in range(N)]

# R昇順
LR.sort(key=lambda x: x[1])


def check(d):
    cnt = 0
    # last_r = -10**18
    last_r = float('-INF')

    for l, r in LR:
        if l >= last_r + d:
            cnt += 1
            last_r = r

            if cnt >= K:
                return True

    return False


# 距離0でもK枚選べないなら答えは-1
if not check(1):   # 非重複条件（共有点もNG）
    print(-1)
    exit()

ok = 1
ng = 10**9 + 1

while ng - ok > 1:
    mid = (ok + ng) // 2

    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)