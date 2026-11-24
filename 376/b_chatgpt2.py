import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

def move(s, b, t):
    return abs((s - b) % N - (t - b) % N)

L, R = 1, 2
ans = 0

for _ in range(Q):
    H, T = input().split()
    T = int(T)

    if H == 'L':
        ans += move(L, R, T)
        L = T
    else:
        ans += move(R, L, T)
        R = T

print(ans)