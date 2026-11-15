import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
A = list(map(int, input().split()))
# print(N, L, R, A)

preA = [0]
for a in A:
  preA.append(preA[-1] + a)
# print(preA)

ans = 0
for i in range(N):
  for j in range(i, N):
    if L <= preA[j + 1] - preA[i] <= R:
      ans += 1

print(ans)