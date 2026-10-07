import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
# print(N, H)

ans = 1
for i in range(1, N):
  for j in range(0, i):
    pre = None
    suc = 1
    for k in range(j, N, i):
      if pre is None:
        pre = H[k]
      else:
        if pre == H[k]:
          suc += 1
          ans = max(ans, suc)
        else:
          pre = H[k]
          suc = 1

print(ans)
