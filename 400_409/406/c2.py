import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
# print(N, P)

pms = []

for i in range(1, N):
  if P[i - 1] < P[i]:
    pms.append('+')
  else:
    pms.append('-')
# print(pms)

succ = 1
prev = None
lan = []
for pm in pms:
  if pm == '+':
    if prev == '+':
      succ += 1
    elif prev == '-':
      lan.append(('-', succ))
      succ = 1
    prev = '+'
  else:
    if prev == '-':
      succ += 1
    elif prev == '+':
      lan.append(('+', succ))
      succ = 1
    prev = '-'
lan.append((prev, succ))
# print(lan)

ans = 0
for i in range(1, len(lan) - 1):
  if lan[i - 1][0] == '+' and lan[i][0] == '-' and lan[i + 1][0] == '+':
    ans += lan[i - 1][1] * lan[i + 1][1]
print(ans)