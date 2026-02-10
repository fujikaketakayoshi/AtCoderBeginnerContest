import sys
input = sys.stdin.readline
import math

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

ans = []
for i in range(1, N + 1):
  ans.append(math.comb(N - len(graph[i]) - 1, 3))

print(' '.join(map(str, ans)))
