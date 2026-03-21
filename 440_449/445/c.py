import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
LOOP = 10 ** 100

graph = [0] * (N + 1)

for i, a in enumerate(A):
  graph[i + 1]= a

ans = []
for s in range(1, N + 1):
  cnt = 0
  start = s
  i = s
  while i != graph[i] or (cnt == 0 and i != start):
    if cnt > 0 and i == start:
      break
    i = graph[i]
    cnt += 1
    # print()
  if i == graph[i]:
    ans.append(i)
  elif cnt > 0 and i == start:
    amari = LOOP % cnt
    for j in range(amari):
      i = graph[i]
    ans.append(i)

print(*ans)
