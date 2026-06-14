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

minY = 3 * 10 ** 5
XYmin = []
for X, Y in XYs:
  minY = min(minY, Y)
  XYmin.append((X, Y, minY))
# print(XYmin)

cnt = 0
for i in range(1, N):
  if XYmin[i][1] > XYmin[i][2]:
      cnt += 1
print(N - cnt)