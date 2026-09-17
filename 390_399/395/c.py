import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

pre_idx = [False] * (10 ** 6 + 1)
# pre_idx = [False] * 56

ans = 10 ** 6
for i, a in enumerate(A):
  idx = i + 1
  if pre_idx[a] != False:
    # print(a, pre_idx[a], idx)
    ans = min(ans, idx - pre_idx[a] + 1)
  pre_idx[a] = idx

# print(pre_idx)
print(-1 if ans == 10 ** 6 else ans)
