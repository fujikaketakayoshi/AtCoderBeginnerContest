import sys
input = sys.stdin.readline
import heapq

X = int(input())
Q = int(input())
# print(X, Q)

small = []
large = []

def addNum(num):
  heapq.heappush(small, -num)
  heapq.heappush(large, -heapq.heappop(small))
  if len(large) > len(small) + 1:
    heapq.heappush(small, -heapq.heappop(large))

addNum(X)

for _ in range(Q):
  A, B = map(int, input().split())
  addNum(A)
  addNum(B)
  print(large[0])
  
