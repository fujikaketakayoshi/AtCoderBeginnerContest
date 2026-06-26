import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)
S = list(input().strip())
T = list(input().strip())
# print(S, T)

bit = 0
for _ in range(M):
  L, R = map(int, input().split())
  L -= 1
  R -= 1
  sbit = '1' * (R - L + 1) + '0' * L
  bit ^= int(sbit, 2)
  # print(bit)

s = f'{bit:0{N}b}'[::-1]
# print(s)
for i, b in enumerate(s):
  if b == '1':
    S[i] = T[i]

print(''.join(S))