import sys
input = sys.stdin.readline

L, R = map(int, input().split())
print(L, R)

# 97, 98, 99

L = 9790

ans = 0
strL = str(L)
lenL = len(strL)
sento = int(strL[0])
lans = None
for i, d in enumerate(strL[1:]):
  d = int(d)
  if not lans:
    lans = max(0, (sento - d) * (int('1' * (lenL - (i + 2))) * (sento - 1) + 1))
  elif lenL - (i + 2) == 0:
    if sento <= d:
      lans -= 10
    else:
      lans -= d
  else:
    if sento <= d:
      lans -= 10 ** (lenL - (i + 1))
    else:
      lans -= d * (int('1' * (lenL - (i + 2))) * (sento - 1) + 1)
  print(d, lans)

print(lans)
