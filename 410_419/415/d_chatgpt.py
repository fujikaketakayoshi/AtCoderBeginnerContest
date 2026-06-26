import sys
input = sys.stdin.readline

N, M = map(int, input().split())

DAB = []

for _ in range(M):
    A, B = map(int, input().split())
    DAB.append((A - B, A))

DAB.sort()
print(DAB)

ans = 0

for d, a in DAB:
    if a > N:
        continue

    x = (N - a) // d + 1
    ans += x
    N -= x * d

print(ans)