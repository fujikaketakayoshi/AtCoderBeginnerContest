import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

bi = 0
x = None

for a in A:
    if bi < N - 1 and a <= B[bi]:
        bi += 1
    elif x is None:
        x = a
    else:
        print(-1)
        exit()

print(x)