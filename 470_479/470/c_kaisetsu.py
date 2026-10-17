input = __import__("sys").stdin.readline
n, q = map(int, input().split())
idxs = []
a = [0] * n
ans = 0
for _ in range(q):
    data = list(map(int, input().split()))
    if data[0] == 1:
        x = data[1] - 1
        if a[x] == 0:
            idxs.append(x)
        ans ^= a[x] ^ (a[x] + 1)
        a[x] += 1
    else:
        for v in idxs:
            ans ^= a[v] ^ (a[v] - 1)
            a[v] -= 1
        idxs = [v for v in idxs if a[v] != 0]
    print(ans)
