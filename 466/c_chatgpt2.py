N = int(input())

r = 2
ans = 0

for l in range(1, N):
    if r < l + 1:
        r = l + 1

    while r <= N:
        print("?", l, r, flush=True)
        res = input().strip()

        if res == "Yes":
            r += 1
        else:
            break
    # print(r - l - 1)
    ans += r - l - 1

print("!", ans, flush=True)