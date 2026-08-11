from collections import Counter

N = int(input())
A = list(map(int, input().split()))

left = Counter()
right = Counter(A)

ans = 0

for i in range(N - 1):
    a = A[i]

    left[a] += 1

    right[a] -= 1
    if right[a] == 0:
        del right[a]

    ans = max(ans, len(left) + len(right))

print(ans)