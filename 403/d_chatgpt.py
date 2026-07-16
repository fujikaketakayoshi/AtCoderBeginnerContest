import sys
input = sys.stdin.readline
from collections import defaultdict

N, D = map(int, input().split())
# print(N, D)
A = list(map(int, input().split()))
A.sort()
# print(A)

cnt = defaultdict(int)
for a in A:
  cnt[a] += 1
# print(cnt)

ans = 0
keys = set(cnt.keys())
# print(keys)
tmp_keys = keys.copy()

if D == 0:
  for k in keys:
    ans += cnt[k] - 1
else:
  for k in tmp_keys:
    tmp = []
    while k in keys:
      keys.remove(k)
      tmp.append((k, cnt[k]))
      k += D
    # print(tmp)
    if len(tmp) == 2:
      ans += min(tmp[0][1], tmp[1][1])
    elif len(tmp) > 2:
      tmpsum = 0
      for k, c in tmp:
        tmpsum += c
      dp = [0] * len(tmp)
      dp[0] = tmp[0][1]
      dp[1] = max(tmp[0][1], tmp[1][1])
      for i in range(2, len(tmp)):
        dp[i] = max(
          dp[i-1],
          dp[i-2] + tmp[i][1]
        )
      ans += tmpsum - dp[-1]
print(ans)