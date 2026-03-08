import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

order = sorted(range(N), key=lambda x: A[x])
print(order)

for _ in range(Q):
    K = int(input())
    B = set(int(x)-1 for x in input().split())

    for i in range(K+1):
        if order[i] not in B:
            print(A[order[i]])
            break
