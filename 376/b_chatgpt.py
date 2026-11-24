import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)

def move(s, b, t):
    for d in [-1, 1]:
        p = s
        cnt = 0
        while p != b:
            if p == t:
                return cnt
            p = (p + d) % N
            cnt += 1
L = 0
R = 1

ans = 0
for _ in range(Q):
  H, T = input().split()
  T = int(T) - 1
  # print(H,T)
  if H == 'L':
    ans += move(L, R, T)
    L = T
  else:
    ans += move(R, L, T)
    R = T
print(ans)