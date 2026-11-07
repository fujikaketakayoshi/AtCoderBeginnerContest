import sys
input = sys.stdin.readline

R = int(input())
print(R)

MAX = 10 ** 6

# print((0.5) ** 2 + (0.5) ** 2, 1 ** 2)
# print((0.5 + 1) ** 2 + (0.5) ** 2, 2 ** 2)
# print((0.5 + 1) ** 2 + (1.5) ** 2, 2 ** 2)
# print((0.5 + 2) ** 2 + (0.5) ** 2, 3 ** 2)
# print((0.5 + 2) ** 2 + (1.5) ** 2, 3 ** 2)
# print((0.5 + 2) ** 2 + (2.5) ** 2, 3 ** 2)

squeres = [[] for _ in range(MAX + 1)]

ans = 1
for r in range(1, R):
  for v in range(R):
    print(0.5 + r, 0.5 + v)
    print((0.5 + r) ** 2 + (0.5 + v) ** 2, (r + 1) ** 2)
    if (0.5 + r) ** 2 + (0.5 + v) ** 2 <= (r + 1) ** 2:
      if squeres[v]:
        print('2', r, v, squeres[v][-1])
        for vv in range(squeres[v][-1] + 1, r + 1):
          print(vv)
          squeres[v].append(vv)
          ans += 4
      else:
        print('1', r, v)
        squeres[v].append(v)
        ans += 4
    else:
      break
print(squeres[:10])
print(ans)