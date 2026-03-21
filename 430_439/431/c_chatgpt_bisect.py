import sys
from bisect import bisect_left
input = sys.stdin.readline

N, M, K = map(int, input().split())
H = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

cnt = 0

for h in H:
    i = bisect_left(B, h)

    if i == len(B):
        continue

    cnt += 1
    B.pop(i)

print("Yes" if cnt >= K else "No")