import sys
input = sys.stdin.readline

N = int(input())
# print(N)

XYs = []
cnt = 0
for _ in range(N):
  X, Y = map(int, input().split())
  XYs.append((X, Y))
XYs.sort()
# print(XYs)

ans = N
minY = float('inf')

for X, Y in XYs:
    if minY < Y:
        ans -= 1
    minY = min(minY, Y)

print(ans)
