import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()
# print(S, T)

def toList(s):
  slist = []
  a_suc = 0
  for c in s:
    if c != 'A':
      slist.append(a_suc)
      slist.append(c)
      a_suc = 0
    else:
      a_suc += 1
  slist.append(a_suc)
  return slist

Slist = toList(S)
Tlist = toList(T)
# print(Slist, Tlist)

if len(Slist) != len(Tlist):
  print(-1)
  exit()

cnt = 0
for i in range(len(Slist)):
  if str(Slist[i]).isdigit() and str(Tlist[i]).isdigit():
    cnt += abs(Slist[i] - Tlist[i])
  elif Slist[i] != Tlist[i]:
    print(-1)
    exit()

print(cnt)
