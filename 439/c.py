import sys
input = sys.stdin.readline

N = int(input().strip())
n = int(N ** 0.5)
print(n)
ans = []
for y in range(n, 0, -1):
  candy = y ** 2
  for x in range(1, n):
    if x >= y:
      break
    candx = x ** 2
    cand = candx + candy
    if cand > N:
      break
    if cand <= N:
      ans.append(cand)

ans.sort()
print(len(ans))
print(*ans)