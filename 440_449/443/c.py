import sys
input = sys.stdin.readline

N, T = map(int, input().split())
A = list(map(int, input().split()))

total = 0
next_open = 0

if len(A) == 0:
    print(T)
    sys.exit()

for a in A:
    if next_open <= a:
        total += a - next_open
        next_open = a + 100

if T - next_open > 0:
    total += T - next_open

print(total)
