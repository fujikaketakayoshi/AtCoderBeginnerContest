import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)

A = [0] * N
Aminus = set()
cnt = [0] * 20

def base_n(num, base):
  if num == 0:
    return "0"
  s = ""
  while num:
    s = str(num % base) + s
    num //= base
  return s

def answer():
  ans = 0
  for i, v in enumerate(cnt):
    ans += (2 ** i) * (v % 2)
  return ans

minus_num = 0
sec_minus = False
for _ in range(Q):
  q = list(map(int, input().split()))
  
  if q[0] == 1:
    sec_minus = False
    idx = q[1] - 1
    if minus_num == 0 or idx in Aminus:
      preb = base_n(A[idx], 2)
      # print(preb)
      for i, b in enumerate(reversed(preb)):
        cnt[i] -= int(b)
      A[idx] += 1
      aftb = base_n(A[idx], 2)
      for i, b in enumerate(reversed(aftb)):
        cnt[i] += int(b)
    elif not idx in Aminus:
      Aminus.add(idx)
      preb = base_n(A[idx] - minus_num, 2)
      # print(preb)
      for i, b in enumerate(reversed(preb)):
        cnt[i] -= int(b)
      A[idx] += 1 - minus_num
      aftb = base_n(A[idx], 2)
      for i, b in enumerate(reversed(aftb)):
        cnt[i] += int(b)
    # print(cnt)
    print(answer())
  else:
    if sec_minus:
      minus_num += 1
    else:
      Aminus = set()
      minus_num = 1
    i = 0
    while i < 20:
      if cnt[i] % 2 == 0:
        i += 1
        continue
      if cnt[i] % 2 == 1:
        for j in range(0, i):
          cnt[j] = 1
        cnt[i] = 0
    sec_minus = True
    # print(cnt)
    print(answer())