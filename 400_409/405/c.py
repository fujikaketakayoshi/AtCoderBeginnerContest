import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

def prefix_sum(arr):
    ps = [0]
    for x in arr:
        ps.append(ps[-1] + x)
    return ps

ps = prefix_sum(A)

ans = 0
for i in range(N - 1):
  ans += A[i] * (ps[N] - ps[i + 1])
print(ans)
