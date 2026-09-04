import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
# print(N, M, A)

# setA = set(A)

QP = {}
for i in range(N):
  QP[Q[i]] = P[i]

for i in range(1, N + 1):
  print(Q[QP[i] - 1])
