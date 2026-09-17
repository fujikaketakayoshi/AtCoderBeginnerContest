import sys
input = sys.stdin.readline

N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))
# print(N, M, B, W)

B.sort(reverse=True)
W.sort(reverse=True)
# print(B)
# print(W)

i = 0
ans = 0
while i < M and i < N:
  if B[i] >= 0 and W[i] >= 0:
    ans += B[i] + W[i]
  elif B[i] >= 0 and W[i] < 0:
    ans += B[i]
  elif B[i] < 0 and B[i] + W[i] >= 0:
    ans += B[i] + W[i]
  i += 1

while i < N:
  if B[i] >= 0:
    ans += B[i]
  i += 1

print(ans)