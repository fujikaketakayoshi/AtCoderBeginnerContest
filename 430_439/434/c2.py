import sys
input = sys.stdin.readline

T = int(input())
# print(T)

for _ in range(T):
  N, H = map(int, input().split())
  # print(N, H)
  target = [(0, H, H)]
  for _ in range(N):
    t, l, u = list(map(int, input().split()))
    target.append([t, l, u])
  # print(target)
  ok = True
  for i in range(len(target) - 1):
    t1, l1, u1 = target[i]
    t2, l2, u2 = target[i + 1]
    diff = t2 - t1
    higher = u1 + diff
    lower = max(l1 - diff, 1)
    # print(higher, lower)
    # print(l2 <= lower <= u2, l2 <= higher <= u2)
    if max(l2, lower) > min(higher, u2):
      ok = False
      break
    r_high = min(higher, u2)
    r_low = max(lower, l2)
    target[i + 1][1] = r_low
    target[i + 1][2] = r_high
    # print(target)
  print('Yes' if ok else 'No')