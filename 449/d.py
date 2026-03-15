import sys
input = sys.stdin.readline

L, R, D, U = map(int, input().split())

cnt = 0
for x in range(L, R + 1):
  for y in range(D, U + 1):
    if max(abs(x),abs(y)) % 2 == 0:
      cnt += 1
print(cnt)