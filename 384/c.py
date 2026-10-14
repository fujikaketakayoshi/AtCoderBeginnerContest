import sys
input = sys.stdin.readline
from collections import defaultdict

scores = list(map(int, input().split()))
# print(scores)
N = len(scores)
name_label = ['A', 'B', 'C', 'D', 'E']
cnt = defaultdict(list)
for S in range(1 << N):
  name = ''
  score = 0
  for i in range(N):     # 各ビットを見る
    if (S >> i) & 1:   # i番目のビットが1なら
      name += name_label[i]
      score += scores[i]
  if name:
    cnt[score].append(name)

for s in sorted(cnt.keys(), reverse=True):
  for name in sorted(cnt[s]):
    print(name)