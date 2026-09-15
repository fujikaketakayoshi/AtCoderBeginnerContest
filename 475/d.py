import sys
input = sys.stdin.readline
from collections import defaultdict

S = input().strip()
N = len(S)

def primes_up_to(n):
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]

primes = set(primes_up_to(10 ** N))
# ans = 10607
# print(ans in primes)


cnt = defaultdict(list)
for i, c in enumerate(S):
  cnt[c].append(i)

keys = list(cnt.keys())
keysn = len(keys)

def dfs(i, tmp):
  if i == keysn:
    ans = int(''.join(map(str, tmp)))
    # print(ans, ans in primes)
    if ans in primes:
      print(ans)
      exit()
    # if ans in primes:
      # print(ans)
      # exit()
    return
  if i == 0:
    for d in range(1, 10):
      for idx in cnt[keys[i]]:
        tmp[idx] = d
      dfs(i + 1, tmp)
  else:
    for d in range(0, 10):
      for idx in cnt[keys[i]]:
        tmp[idx] = d
      dfs(i + 1, tmp)

dfs(0, [None] * N)
print(-1)