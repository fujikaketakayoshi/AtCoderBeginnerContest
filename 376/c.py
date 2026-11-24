import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(N, A, B)

A.sort()
B.sort()
# print(A)
# print(B)

ai = N - 1
bi = N - 2
x = None
while ai >= 0 and bi >= -1:
  # print(ai, bi)
  if ai == 0 and bi == -1:
    x = A[ai]
    break
  elif A[ai] <= B[bi]:
    ai -= 1
    bi -= 1
    continue
  elif A[ai] > B[bi] and x is None:
    x = A[ai]
    ai -= 1
  elif A[ai] > B[bi] and x is not None:
    print(-1)
    exit()
# print(ok, x)
print(x)