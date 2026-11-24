import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)

def right(L, R, T):
  cnt = 0
  r = R
  while r != L:
    if r == T:
      return cnt
    cnt += 1
    r -= 1
    if r == 0:
      r = N
  cnt = 0
  r = R
  while r != L:
    if r == T:
      return cnt
    cnt += 1
    r += 1
    if r == N + 1:
      r = 1

def left(L, R, T):
  cnt = 0
  l = L
  while l != R:
    if l == T:
      return cnt
    cnt += 1
    l -= 1
    if l == 0:
      l = N
  cnt = 0
  l = L
  while l != R:
    if l == T:
      return cnt
    cnt += 1
    l += 1
    if l == N + 1:
      l = 1

L = 1
R = 2

ans = 0
for _ in range(Q):
  H, T = input().split()
  T = int(T)
  # print(H,T)
  if H == 'L':
    ans += left(L, R, T)
    L = T
  else:
    ans += right(L, R, T)
    R = T
print(ans)