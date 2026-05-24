import sys
input = sys.stdin.readline

N = int(input())
# C = []
# for _ in range(N - 1):
#   C.append(list(map(int, input().split())))
C=[[None]*(i+1)+list(map(int,input().split())) for i in range(N-1)]

for a in range(0, N - 2):
  for b in range(a + 1, N - 1):
    for c in range(b + 1, N):
      # print(a, b, c)
    #   if C[a][c - a - 1] > C[a][b - a - 1] + C[b][c - b - 1]:
      if C[a][c] > C[a][b] + C[b][c]:
        print('Yes')
        exit()
print('No')