import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(N, M, K, H, B)

H.sort(reverse=True)
B.sort(reverse=True)
# print(H, B)

j = 0
cnt = 0
for h in H:
  while j < M:
    print(h, B[j])
    if h <= B[j]:
      cnt += 1
      j += 1
      break
    j += 1
print('Yes' if cnt >= K else 'No')