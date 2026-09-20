import sys
input = sys.stdin.readline
# import heapq

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

nums = A[:3]
nums.sort()
print(nums[0])

for i in range(3, N):
  nums.append(A[i])
  nums.sort()
  nums = nums[1:]
  print(nums[0])