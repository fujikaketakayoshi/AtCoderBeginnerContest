import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

xors = set()

base = 0
for a in A:
  base ^= a
# print(base)
xors.add(base)

used = [False] * N

def dfs(cnt, tmp):
  global base
  if cnt >= N - 1:
    return
  for i in range(N):
    if tmp[i] == 0:
      continue
    diff = tmp[i]
    tmp[i] = 0
    used[i] = True
    for j in range(N):
      if used[j] or tmp[j] == 0:
        continue
      xor = base
      beforej = tmp[j]
      tmp[j] += diff
      xor ^= diff ^ beforej ^ tmp[j]
      # print(i, j, tmp, xor)
      xors.add(xor)
      dfs(cnt + 1, tmp)
      tmp[j] -= diff
    used[i] = False
    tmp[i] = diff

dfs(0, A[:])
print(len(xors))
