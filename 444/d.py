import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)

for a in A:
  cnt[a] += 1

total = 0
for k, v in cnt.items():
  total += int('1' * k) * v

print(total)
