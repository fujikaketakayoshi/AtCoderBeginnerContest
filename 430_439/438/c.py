import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

stack = []

for a in A:
  stack.append(a)
  if len(stack) >= 4 and stack[-1] == stack[-2] == stack[-3] == stack[-4]:
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()

print(len(stack))