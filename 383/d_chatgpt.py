import math

N = int(input())
R = math.isqrt(N)

# エラトステネスの篩
is_prime = [True] * (R + 1)
is_prime[0] = is_prime[1] = False

for p in range(2, math.isqrt(R) + 1):
    if is_prime[p]:
        for j in range(p * p, R + 1, p):
            is_prime[j] = False

primes = [p for p in range(2, R + 1) if is_prime[p]]

ans = 0

# パターン1: p^2 * q^2
for i in range(len(primes)):
    p = primes[i]

    for j in range(i + 1, len(primes)):
        q = primes[j]

        if p * q > R:
            break

        ans += 1

# パターン2: p^8
for p in primes:
    if p ** 4 > R:
        break

    ans += 1

print(ans)