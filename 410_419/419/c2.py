import sys
input = sys.stdin.readline

N = int(input())
# print(N)

minR = 10**18
maxR = -1
minC = 10**18
maxC = -1

for _ in range(N):
    R, C = map(int, input().split())
    minR = min(minR, R)
    maxR = max(maxR, R)
    minC = min(minC, C)
    maxC = max(maxC, C)

cnt_R = (maxR - minR + 2 - 1) // 2
cnt_C = (maxC - minC + 2 - 1) // 2

print(max(cnt_R, cnt_C))