import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
  N, D = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  eggs = []
  idx = 0
  total = 0
  for i in range(N):
    eggs.append(A[i])
    total += A[i]
    tmp_B = B[i]
    total -= B[i]
    while eggs:
      if eggs[idx] >= tmp_B:
        eggs[idx] -= tmp_B
        if eggs[idx] == 0:
          idx += 1
        break
      else:
        tmp_B -= eggs[idx]
        eggs[idx] = 0
        idx += 1
    
    if i - D >= 0:
      total -= eggs[i - D]
      eggs[i - D] = 0
  print(total)