import sys
input = sys.stdin.readline
from bisect import bisect_right

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = []
mi = float('inf')

for a in A:
    mi = min(mi, a)
    C.append(mi)

C.reverse()

for b in B:
    idx = bisect_right(C, b)

    if idx == 0:
        print(-1)
    else:
        print(N - idx + 1)