import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# print(N, K)
lenA = 2 ** N

shou = K // lenA
amari = K % lenA
U = 0 if amari == 0 else 1

A = [shou] * lenA

if amari > 0:
  ok = True
  for i in range(N):
    b, c =  2 ** i, 2 ** (i + 1)
    # print(b, c)
    for j in range(lenA):
      if j % c == b:
        A[j] += 1
        amari -= 1
        if amari == 0:
          ok = False
          break
    if not ok:
      break
print(U)
print(*A)