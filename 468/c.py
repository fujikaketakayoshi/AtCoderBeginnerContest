import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
print(N, P, Q)

def permutation_num(n, k):
	"""Return number of permutations P(n, k) = n! / (n-k)!."""
	if not isinstance(n, int) or not isinstance(k, int):
		raise TypeError("n and k must be integers")
	if n < 0 or k < 0:
		raise ValueError("n and k must be non-negative")
	if k > n:
		return 0
	result = 1
	for i in range(n, n - k, -1):
		result *= i
	return result


i = 0
top = 0
while i < N:
  if P[i] == Q[i]:
    i += 1
    continue
  elif P[i] > Q[i]:
    print(0)
    exit()
  else:
    top = i
    break

ans = 0
Pcnt = Q[top] - P[top]
chukan = 1
print(chukan)
ans += chukan * permutation_num(N - top - 1, N - top - 1)

Pcnt = 1
Qcnt = 1
for i in range(top + 1, N):
  Pcnt *= N - P[i] + 1
  Qcnt *= Q[i]
print(Pcnt, Qcnt)