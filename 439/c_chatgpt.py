import sys
input = sys.stdin.readline

N = int(input().strip())
n = int(N ** 0.5)

cnt = [0] * (N + 1)

for y in range(1, n + 1):
    y2 = y * y
    for x in range(1, y):
        cand = x * x + y2
        if cand > N:
            break
        cnt[cand] += 1

ans = [i for i in range(1, N + 1) if cnt[i] == 1]

print(len(ans))
print(*ans)
