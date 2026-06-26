import sys
input = sys.stdin.readline

N = int(input())
# print(N)

Rs = []
Cs = []
for _ in range(N):
  R, C = map(int, input().split())
  Rs.append(R)
  Cs.append(C)

min_R = min(Rs)
max_R = max(Rs)
min_C = min(Cs)
max_C = max(Cs)
# print(min_R, max_R, min_C, max_C)

diff_R = max_R - min_R
diff_C = max_C - min_C

cnt_R = diff_R // 2
cnt_C = diff_C // 2

if diff_R % 2 == 1:
  cnt_R += 1
if diff_C % 2 == 1:
  cnt_C += 1

print(max(cnt_R, cnt_C))