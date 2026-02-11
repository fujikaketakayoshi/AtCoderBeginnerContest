import sys
input = sys.stdin.readline

N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

# prefix sum
pref = [0] * (N + 1)
for i in range(N):
    pref[i+1] = pref[i] + A[i]

water = N - K

ans = -1

for m in range(1, N + 1):
    s = max(0, m - water)  # 最低保証される日本酒の個数
    if s == 0:
        continue

    # 大きい方から m 個 → A[N-m ... N-1]
    # その中で小さい方から s 個
    left = N - m
    right = left + s

    sake_sum = pref[right] - pref[left]

    if sake_sum >= X:
        ans = m
        break

print(ans)
