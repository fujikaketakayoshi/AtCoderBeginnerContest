N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

K = max(B)
ans = [-1] * (K + 1)

r = K

for i, a in enumerate(A):
    while r >= a:
        ans[r] = i + 1
        r -= 1

for b in B:
    print(ans[b])