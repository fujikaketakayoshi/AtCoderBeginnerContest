import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque

N = int(input())
master = set()

cnt = defaultdict(list)
q = deque()

for n in range(1, N + 1):
  A, B = map(int, input().split())
  if A == 0 and B == 0:
    master.add(n)
    q.append(n)
  else:
    cnt[A].append(n)
    cnt[B].append(n)

while q:
  m = q.popleft()
  for n in cnt[m]:
    if not n in master:
      master.add(n)
      q.append(n)

print(len(master))