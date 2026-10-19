import sys
input = sys.stdin.readline

N, K, T = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print(N, K, T, A)
B = []
for a in A:
  if a < T:
    B.append(a)

ans = 0
nt = 0
for b in B:
  if nt < b:
    ans += (b - nt + K - 1) // K
    # print(nt, a, a - nt, (a - nt + K - 1) // K)
  # print(b, nt, b - nt, (b - nt + K - 1) // K)
  nt = b + K
  
  if T <= nt:
    break

if nt < T:
  ans += (T - nt + K - 1) // K
# print(T, nt, T - nt, (T - nt + K - 1) // K)
print(ans)