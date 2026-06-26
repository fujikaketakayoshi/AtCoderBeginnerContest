import sys
input = sys.stdin.readline

N, K, X = map(int, input().split())

Ss = [input().strip() for _ in range(N)]
Ss.sort()

X -= 1  # 0-indexed にする

ans = []

for i in range(K):
    block = N ** (K - 1 - i)

    idx = X // block
    ans.append(Ss[idx])

    X %= block

print("".join(ans))