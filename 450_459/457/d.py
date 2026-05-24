import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
# print(N, K)
A = list(map(int, input().split()))
# print(A)

n = N * (N + 1) // 2

nokori = K % n
matome = K // n
print(n, nokori, matome)


hq = []  # 空のヒープを作る
for i, a in enumerate(A):
  heapq.heappush(hq, (a, i + 1))

for k in range(K):
  x, i = heapq.heappop(hq)
  heapq.heappush(hq, (x + i, i))

print(hq[0][0])
