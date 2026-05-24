import sys
input = sys.stdin.readline

MOD = 998244353

S = input().strip()
# print(S)

n = len(S)

succ = 1
Ss = []
for i in range(n - 1):
  if S[i] == S[i + 1]:
    succ += 1
  else:
    Ss.append(succ)
    succ = 1
Ss.append(succ)
# print(Ss)

cnt = 0
dcnt = 0
for i, s in enumerate(Ss):
  dcnt += 1
  if s > 1:
    cnt += dcnt * (dcnt + 1) // 2 + s - 2
    dcnt = 1
cnt += dcnt * (dcnt + 1) // 2

print(cnt % MOD)