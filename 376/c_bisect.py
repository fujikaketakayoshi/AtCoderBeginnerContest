import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

def check(x):
    C = sorted(B + [x])
    return all(a <= c for a, c in zip(A, C))

ng = 0
ok = 10**9

if not check(ok):
    print(-1)
    exit()

while ok - ng > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)