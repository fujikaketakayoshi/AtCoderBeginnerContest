import sys
input = sys.stdin.readline

S = input().strip()
# print(S, S[:-1])

btnB = 0
amari = 0
for i in range(len(S) - 1, -1, -1):
  d = int(S[i])
  if d >= amari:
    btnB += d - amari
  else:
    btnB += d + 10 - amari
  amari = btnB % 10
print(len(S) + btnB)
