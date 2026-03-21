import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

reach = 1 + A[0] - 1  # 1番目の影響

i = 2
while i <= reach and i <= N:
    reach = max(reach, i + A[i-1] - 1)
    i += 1

print(min(reach, N))