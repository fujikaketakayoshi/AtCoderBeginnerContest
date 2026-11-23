import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
# print(N, M)

graph = [[] for _ in range(N)]

for _ in range(M):
  U, V, C = map(int, input().split())
  U -= 1
  V -= 1
  graph[U].append((V, C))

# print(graph)

q = deque()
q.append((0, 0, -1))
first = [-2] * N
second = [False] * N

first[0] = -1
q = deque([(0, 0, -1)])

while q:
    u, cnt, prec = q.popleft()

    if u == N - 1:
        print(cnt)
        exit()

    for v, c in graph[u]:
        if c == prec:
            continue

        if first[v] == -2:
            first[v] = c
        elif c == first[v] or second[v]:
            continue
        else:
            second[v] = True

        q.append((v, cnt + 1, c))

print(-1)