import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# print(N, K)

arr = [0] * 10
for i in range(1, N + 1):
  arr[i - 1] = K // i

# print(arr)

ans = []
s = 0
for i1 in range(arr[0] + 1):
  for i2 in range(arr[1] + 1):
    for i3 in range(arr[2] + 1):
      for i4 in range(arr[3] + 1):
        for i5 in range(arr[4] + 1):
          for i6 in range(arr[5] + 1):
            for i7 in range(arr[6] + 1):
              for i8 in range(arr[7] + 1):
                for i9 in range(arr[8] + 1):
                  for i10 in range(arr[9] + 1):
                    s = i1 * 1 + i2 * 2 + i3 *3 + i4 * 4 + i5 * 5 + i6 * 6 + i7 * 7 + i8 * 8 + i9 *9 + i10 * 10
                    if s == K:
                      tmp = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
                      print(*tmp[:N])
