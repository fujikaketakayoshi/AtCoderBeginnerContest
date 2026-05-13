import sys
input = sys.stdin.readline

N, R = map(int, input().split())
L = list(map(int, input().split()))

left = list(reversed(L[:R]))
right = L[R:]
# print(left, right)

def door_num(arr):

  while len(arr) > 0 and arr[-1] == 1:
    arr.pop()
  # print(arr)
  
  cnt = 0
  for a in arr:
    if a == 0:
      cnt += 1
    else:
      cnt += 2
  return cnt

cnt = door_num(left)
cnt += door_num(right)
print(cnt)