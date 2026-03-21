import sys
input = sys.stdin.readline

N = int(input().strip())

jijo = []
for i in range(1, N):
  v = i ** 2
  if v >= N:
    break
  jijo.append(v)

n = len(jijo)
ans = []
for i in range(n - 1, -1, -1):
  for j in range(0, n):
    if j >= i:
      break
    cand = jijo[i] + jijo[j]
    if cand > N:
      break
    ans.append(cand)

ans.sort()
print(len(ans))
print(*ans)
