import sys
input = sys.stdin.readline
import heapq

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

hq = A[:3]
heapq.heapify(hq)

print(hq[0])

for i in range(3, N):
  heapq.heappush(hq, A[i])
  heapq.heappop(hq)
  print(hq[0])