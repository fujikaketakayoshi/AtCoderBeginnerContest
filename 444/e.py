import sys
input = sys.stdin.readline

N, D = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
l, r = 0, 0

while l < N:
  while r < N:
    if l == r:
      cnt += 1
      r += 1
    else:
      if abs(A[l] - A[r]) < D:
        l += 1
        r = l
        break
      else:
        cnt += 1
        r += 1
  l += 1
  

print(cnt)
