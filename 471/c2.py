import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

Ap = [float('INF')]
Am = [float('-INF')]

for a in A:
  if a > 0:
    Ap.append(a)
  else:
    Am.append(a)

Ap.sort(reverse=True)
Am.sort()

# print(Ap)
# print(Am)

i = 0
ans = 0
while len(Ap) > 1 or len(Am) > 1:
  pd = Ap[-1] - i
  md = -Am[-1] + i
  if pd >= md:
    ans += md
    i = Am.pop()
  else:
    ans += pd
    i = Ap.pop()
print(ans)
  