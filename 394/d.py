import sys
input = sys.stdin.readline

S = input().strip()
# print(S)

q = []

for c in S:
  if len(q) > 0 and ((q[-1] == '(' and c == ')') or  (q[-1] == '[' and c == ']') or (q[-1] == '<' and c == '>')):
    q.pop()
    continue
  else:
    q.append(c)

print('Yes' if len(q) == 0 else 'No')