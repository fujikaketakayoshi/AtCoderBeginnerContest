import sys
input = sys.stdin.readline

N, K = map(int, input().split())

A = [0] * N

def dfs(i, remain):
    # 最後の1要素は計算で決める
    if i == N - 1:
        if remain % N == 0:
            A[i] = remain // N
            print(*A)
        return

    weight = i + 1

    for x in range(remain // weight + 1):
        A[i] = x
        dfs(i + 1, remain - weight * x)

dfs(0, K)