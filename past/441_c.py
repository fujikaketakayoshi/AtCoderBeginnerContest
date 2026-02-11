import sys
input = sys.stdin.readline
from collections import deque

N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

water_ok = N - K

stack = deque(A)

for i in range(water_ok):
  stack.pop()

total = 0
cnt = 0
while stack:
  sake_able = stack.pop()
  total += sake_able
  cnt += 1
  if total >= X:
    break

print(cnt + water_ok if total >= X else -1)

