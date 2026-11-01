import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
# print(N,X)

for k in range(N):
  t1 = 0
  t2 = 0
  if k == 0 or k == N - 1:
    print((X[-1] - X[0]) // 2)
  else:
    t1 += (X[k + 1] - X[k]) // 2
    ld = (X[k] + t1) - (X[0] + t1)
    rd = (X[-1] - t1) - (X[k] + t1)
    # print(t1, X[k] + t1, ld, rd)
    t1 += max(ld, rd) // 2
    
    t2 += (X[k] - X[k - 1]) // 2
    ld = (X[k - 1] + t2) - (X[0] + t2)
    rd = (X[-1] - t2) - (X[k - 1] + t2)
    # print(t2, X[k] + t2, ld, rd)
    t2 += max(ld, rd) // 2
    print(min(t1, t2))