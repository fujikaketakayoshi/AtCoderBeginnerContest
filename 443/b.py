import sys
input = sys.stdin.readline

N, K = map(int, input().split())

i = 0
total = 0
while total < K:
    total += N + i
    i += 1

print(i - 1)