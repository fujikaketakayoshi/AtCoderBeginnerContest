import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

B = []
cnt = {}
for i in range(N):
  idx = cnt[A[i]] if A[i] in cnt else -1
  cnt[A[i]] = i + 1
  B.append(idx)

print(*B)