N = int(input())

r = 1
ans = 0

for l in range(1, N):
    if r < l:
        r = l

    while r + 1 <= N:
        print("?", l, r + 1, flush=True)
        res = input().strip()

        if res == "Yes":
            r += 1
        else:
            break
    print(r - l)
    ans += r - l

print("!", ans, flush=True)