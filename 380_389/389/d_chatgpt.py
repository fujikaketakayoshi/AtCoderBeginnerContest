R = int(input())

ans = 1
y = R - 1

for x in range(1, R):
    while y >= 0 and (2*x + 1)**2 + (2*y + 1)**2 > 4*R**2:
        y -= 1

    ans += (y + 1) * 4

print(ans)