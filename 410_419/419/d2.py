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
  r = 2 ** (R + 1) - 1
  l = 2 ** L - 1
  # print(f'{r:0{N}b}')
  # print(f'{l:0{N}b}')
  # print(r ^ l)
  
  bit ^= r ^ l
  # print(bit)

for i in range(N):
  if (bit >> i) & 1:
    # print(i)
    S[i] = T[i]

print(''.join(S))