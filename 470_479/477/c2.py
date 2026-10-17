import sys
input = sys.stdin.readline

Q = int(input())
S = input().strip()
T = input().strip()
# print(Q, S, T)
N = len(S)
lenT = len(T)

idxs = [0] * N
for i in range(N - lenT + 1):
  idxs[i] = 1 if S[i:i + lenT] == T else 0
# print(idxs)

pre = [0] * (N + 1)
for i in range(len(idxs)):
  pre[i + 1] = pre[i] + idxs[i]
# print(pre)

for _ in range(Q):
  L, R = map(int, input().split())
  if R - L + 1 < lenT:
    print('No')
    continue
  
  left = L - 1
  right = R - 1 - (lenT - 1)
  # print(L, R, left, right, pre[right + 1] - pre[left])
  if pre[right + 1] - pre[left] > 0:
    print('Yes')
  else:
    print('No')
