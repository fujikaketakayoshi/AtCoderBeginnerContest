import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

ans = 0
aidx = N - 1
for b in reversed(A):
  while aidx >= 0:
    a = A[aidx]
    if 2 * a <= b:
      ans += aidx + 1
      break
    aidx -= 1

print(ans)