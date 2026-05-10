import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# print(N, K)

L = []
for _ in range(N):
  LA = list(map(int, input().split()))
  L.append(LA[1:])
# print(L)

C = list(map(int, input().split()))

for i, c in enumerate(C):
  l = len(L[i]) * c
  if K - l <= 0:
    tmp = L[i] * c
    # print(tmp)
    # print()
    print(tmp[K - l - 1])
    exit()
  K -= l
