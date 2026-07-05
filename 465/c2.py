import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

left = []
right = []
pre = False
for i in range(len(S) - 1, -1, -1):
  if S[i] == 'o':
    pre = not pre
  if pre:
    left.append(i + 1)
  else:
    right.append(i + 1)

right.reverse()
print(*(left + right))