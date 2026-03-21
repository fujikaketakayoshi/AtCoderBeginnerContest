import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    R = list(map(int, input().split()))

    len_R = len(R)
    cnt = 0
    for i in range(len_R - 1):
        diff = R[i] - R[i + 1]
        if diff < -1:
            R[i + 1] -= abs(diff) - 1
            cnt += abs(diff) - 1
    
    for i in range(len_R - 1, 0, -1):
        diff = R[i] - R[i - 1]
        if diff < -1:
            R[i - 1] -= abs(diff) - 1
            cnt += abs(diff) - 1

    print(cnt)
