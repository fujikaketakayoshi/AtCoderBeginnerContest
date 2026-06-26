import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = list(input().strip())
T = input().strip()

diff = [0] * (N + 1)

for _ in range(M):
    L, R = map(int, input().split())
    L -= 1
    R -= 1

    diff[L] ^= 1
    diff[R + 1] ^= 1

cur = 0
print(diff)

for i in range(N):
    cur ^= diff[i]

    if cur:
        S[i] = T[i]

print(''.join(S))