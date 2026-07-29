import sys
input = sys.stdin.readline

N = int(input())
# print(N)

MAX = 10 ** 18

cnt = set()

for a in range(1, MAX):
  Xa = 2 ** a
  if Xa > N:
    break
  cnt.add(Xa)

ans = set()
for b in range(1, 10 ** 9):
  Xb = b ** 2
  if Xb < N:
    for Xa in cnt:
      X = Xa * Xb
      if X > N:
        break
      ans.add(X)

print(len(ans))
