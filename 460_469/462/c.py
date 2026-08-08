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

cnt = 0
for i in range(1, N):
  for j in range(0, i):
    # print(XYs[j][1], XYs[i][1], 0 < XYs[j][1] < XYs[i][1])
    if 0 < XYs[j][1] < XYs[i][1]:
      cnt += 1
      break
print(N - cnt)
