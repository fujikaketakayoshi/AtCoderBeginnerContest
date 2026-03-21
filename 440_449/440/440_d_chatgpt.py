import sys
input = sys.stdin.readline
import bisect

N, Q = map(int, input().split())
A = sorted(map(int, input().split()))

for _ in range(Q):
    X, Y = map(int, input().split())
    
    # X未満の欠番数
    base = (X - 1) - bisect.bisect_right(A, X - 1)
    
    # 二分探索
    left = X
    right = 2 * 10 ** 9  # 十分大きい
    
    while left < right:
        mid = (left + right) // 2
        missing = (mid - bisect.bisect_right(A, mid)) - base
        
        if missing >= Y:
            right = mid
        else:
            left = mid + 1
    
    print(left)
