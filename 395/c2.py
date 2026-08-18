import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

pre_idx = [None] * (10 ** 6 + 1)
# pre_idx = [False] * 56

ans = N + 1
for i, a in enumerate(A):
  if pre_idx[a] is not None:
    # print(a, pre_idx[a], idx)
    ans = min(ans, i - pre_idx[a] + 1)
  pre_idx[a] = i

# print(pre_idx)
print(-1 if ans == N + 1 else ans)
