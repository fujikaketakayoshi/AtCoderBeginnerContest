import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

pos = [0]
for i, c in enumerate(S):
    if c == 'x':
        pos.append(i)

for k in range(1, N + 1):
    if k > len(pos):
        print(N)
    else:
        print(pos[k] + 1)