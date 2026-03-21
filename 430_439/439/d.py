import sys
input = sys.stdin.readline
from collections import defaultdict
import bisect

N = int(input().strip())
A = list(map(int, input().split()))

waru7 = defaultdict(list)
waru5 = defaultdict(list)
waru3 = defaultdict(list)

for i, v in enumerate(A):
  if v % 7 == 0:
    waru7[v // 7].append(i) 
  if v % 5 == 0:
    waru5[v // 5].append(i) 
  if v % 3 == 0:
    waru3[v // 3].append(i) 

cnt = 0
for b in waru7.keys():
  # print(waru7[b], waru5[b], waru3[b])
  if waru5[b] and waru3[b]:
    for j in waru5[b]:
      idx7l = bisect.bisect_left(waru7[b], j)
      # print(j, idx7, waru7[b])
      cnt7l = len(waru7[b]) - idx7l
      idx3l = bisect.bisect_left(waru3[b], j)
      # print(j, idx3, waru3[b])
      cnt3l = len(waru3[b]) - idx3l
      cnt += cnt7l * cnt3l
      idx7r = bisect.bisect_right(waru7[b], j)
      idx3r = bisect.bisect_right(waru3[b], j)
      cnt += idx7r * idx3r

      
print(cnt)
