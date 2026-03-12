import sys
input = sys.stdin.readline

N, X, Y = map(int, input().split())
print(N, X, Y)
kukans = [(0, X - 1, 0, Y - 1)]
print(kukans)

def bunkatu(kukans):
  new_kukan = []
  for kukan in kukans:
    x1, x2, y1, y2 = kukan
    lx = x2 - x1
    ly = y2 - y1
    if x1 <= A <= x2:
      n1x2 = x2 - (A - 1)
      n1x1 = x1
      n2x1 = n1x2 + 1
      n2x2 = x2
      n1y1 = B - ly
      n1y2 = B
      n2y1 = B + ly
      n2y2 = B
      new_kukan.append((n1x1, n1x2, n1y1, n1y2))
      new_kukan.append((n2x1, n2x2, n2y1, n2y2))
    else:
      new_kukan.append(kukan)
  return new_kukan

for _ in range(N):
  C, A, B = list(map(str, input().split()))
  A, B = int(A), int(B)
  print(C, A, B)
