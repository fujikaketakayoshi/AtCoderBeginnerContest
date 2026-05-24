import sys
input = sys.stdin.readline

MOD = 998244353

N = int(input())

children = [[] for _ in range(N)]

P = list(map(int, input().split()))

for i, p in enumerate(P, start=1):
    children[p - 1].append(i)

C = list(map(int, input().split()))
D = list(map(int, input().split()))

MAXD = sum(D)

# inv[i] = i^{-1}
inv = [1] * (MAXD + 1)

for i in range(2, MAXD + 1):
    inv[i] = MOD - MOD // i * inv[MOD % i] % MOD


def comb_large_n_small_r(n, r):
    """
    n is huge
    r is <= 1e6
    """

    if r < 0 or r > n:
        return 0

    res = 1

    for i in range(r):
        res *= (n - i) % MOD
        res %= MOD

    for i in range(1, r + 1):
        res *= inv[i]
        res %= MOD

    return res


need = [0] * N
candy = [0] * N

# iterative postorder DFS
order = []
stack = [0]

while stack:
    u = stack.pop()
    order.append(u)

    for v in children[u]:
        stack.append(v)

# postorder
order.reverse()
print(order)

ans = 1

for u in order:

    total_need = D[u]
    total_candy = C[u]

    child_need = 0

    for v in children[u]:
        total_need += need[v]
        total_candy += candy[v]
        child_need += need[v]

    need[u] = total_need
    candy[u] = total_candy

    # impossible
    if need[u] > candy[u]:
        print(0)
        exit()

    available = candy[u] - child_need

    ans *= comb_large_n_small_r(available, D[u])
    ans %= MOD

print(ans)