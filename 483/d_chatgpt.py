import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

xs = []
x = 0
for a in A:
  x += a
  xs.append(x)

# print(xs)
maxs = []
mins = []
ma = float('-inf')
mi = float('inf')
for x in reversed(xs):
  if x < mi:
    mi = x
  if x > ma:
    ma = x
  maxs.append(ma)
  mins.append(mi)
maxs.reverse()
mins.reverse()
# print(maxs)
# print(mins)
# print(ma, mi)

left_max = 0
left_min = 0
ans = max(0, maxs[0]) - min(0, mins[0]) + 1

for i in range(N):
    shift = -2 * A[i]

    hi = max(left_max, maxs[i] + shift)
    lo = min(left_min, mins[i] + shift)

    ans = max(ans, hi - lo + 1)

    left_max = max(left_max, xs[i])
    left_min = min(left_min, xs[i])
print(ans)