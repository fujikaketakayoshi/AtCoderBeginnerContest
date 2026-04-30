import sys
input = sys.stdin.readline

T = int(input())
# print(T)

for _ in range(T):
  na, nb, nc = map(int, input().split())
  # print(na, nb, nc)
  common_ac = min(na, nc)
  na -= common_ac
  nc -= common_ac
  
  cnt = min(common_ac, na + nb + nc)
  print(cnt)
