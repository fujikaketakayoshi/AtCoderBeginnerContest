import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
print(N, Q)
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(A, B)

graph = [[] for _ in range(N + 2)]
for i in range(1, N + 1):
  graph[i].append({(i % N) + 1: A[i - 1]})
  graph[(i % N) + 1].append({i: A[i - 1]})
  graph[i].append({N + 1: B[i - 1]})
  graph[N + 1].append({i: B[i - 1]})
print(graph)



for _ in range(Q):
  S, T = map(int, input().split())
  print(S, T)
