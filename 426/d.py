import sys
input = sys.stdin.readline

T = int(input())
# print(T)

for _ in range(T):
  N = int(input())
  S = input().strip()
  # print(N, S)
  arr = []
  i = 1
  prev = S[0]
  succ = 1
  while i < N:
    if prev == S[i]:
      succ += 1
    else:
      arr.append((prev, succ))
      prev = S[i]
      succ = 1
    i += 1
  arr.append((prev, succ))
  # print(arr)
  n = len(arr)
  if n == 1:
    print(0)
    continue
  mid = n // 2 - 1
  cnt1 = 0
  for i, (s, num) in enumerate(arr):
    if i < mid:
      cnt1 += (mid - i) * num
    elif i == mid:
      continue
    else:
      cnt1 += (i - mid) * num
  mid = n // 2
  cnt2 = 0
  for i, (s, num) in enumerate(arr):
    if i < mid:
      cnt2 += (mid - i) * num
    elif i == mid:
      continue
    else:
      cnt2 += (i - mid) * num
  print(min(cnt1, cnt2))
