import sys
input = sys.stdin.readline
import bisect

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

ans = 0
for b in A:
  idx = bisect.bisect_right(A,  b / 2)
  ans += idx

print(ans)