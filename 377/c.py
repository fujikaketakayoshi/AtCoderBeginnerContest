import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

DIRS = [
  (2, 1),
  (1, 2),
  (-1, 2),
  (-2, 1),
  (-2, -1),
  (-1, -2),
  (1, -2),
  (2, -1),
]

ans = set()
for _ in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  ans.add((a, b))
  for dy, dx in DIRS:
    ny = a + dy
    nx = b + dx
    if 0 <= ny < N and 0 <= nx < N:
      ans.add((ny, nx))


# print(ans)
print(N * N - len(ans))
    