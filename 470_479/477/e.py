import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
print(N, Q)
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(A, B)

graph = [[] for _ in range(N + 1)]
for i in range(N):
  graph[i].append({(i % (N)) + 1: A[i]})
  graph[(i % (N)) + 1].append({i: A[i]})
  graph[i].append({N: B[i]})
  graph[N].append({i: B[i]})
print(graph)



for _ in range(Q):
  S, T = map(int, input().split())
  print(S, T)
  if T == N - 1:
    1
  elif S == T - 1:
    1
