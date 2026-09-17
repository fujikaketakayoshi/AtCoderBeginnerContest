import sys
input = sys.stdin.readline

N, W = map(int, input().split())
# print(N, W)

blocksW = [[] for _ in range(W + 1)]
blocksWnum = [0] * (W + 1)
for i in range(N):
  X, Y = map(int, input().split())
  blocksW[X].append((Y, i + 1))
  blocksWnum[X] += 1
# print(blocksW)
# print(blocksWnum)
eraseH = min(blocksWnum[1:])
# print(eraseH)

for w in range(W + 1):
  blocksW[w].sort()
# print(blocksW)

initialRm = True
for w in range(W + 1):
  if blocksW[w] and blocksW[w][0][0] != 1:
    initialRm = False

eraseTime = [10 ** 9 + 1] * (N + 1)
for w in range(W + 1):
  for h, yn in enumerate(blocksW[w]):
    # print(h, yn)
    # rmLimit = blocksWnum[w] - eraseH
    if h + 1 <= eraseH:
      if initialRm:
        eraseTime[yn[1]] = h + 1
      else:
        eraseTime[yn[1]] = h + 1 + 1
# print(eraseTime)

Q = int(input())
# print(Q)

for _ in range(Q):
  T, A = map(int, input().split())
  # print(T, A, 'Yes' if T < eraseTime[A] else 'No')
  print('Yes' if T < eraseTime[A] else 'No')