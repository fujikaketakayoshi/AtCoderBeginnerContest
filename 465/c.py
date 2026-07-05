import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

left = []
right = []
pre = 'r'
for i in range(len(S) - 1, -1, -1):
  if S[i] == 'o' and pre == 'r':
    # print('[1]', i + 1, S[i], pre)
    left.append(i + 1)
    pre = 'l'
  elif S[i] == 'x' and pre == 'r':
    # print('[2]', i + 1, S[i], pre)
    right.append(i + 1)
  elif S[i] == 'o' and pre == 'l':
    # print('[3]', i + 1, S[i], pre)
    right.append(i + 1)
    pre = 'r'
  elif S[i] == 'x' and pre == 'l':
    # print('[4]', i + 1, S[i], pre)
    left.append(i + 1)

right.reverse()
print(*(left + right))