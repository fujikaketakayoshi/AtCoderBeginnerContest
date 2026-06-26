import sys
input = sys.stdin.readline

N = int(input())
T = input().strip()

# 最初に「まだ0を1個も見ていない状態（0個=偶数）」が1回あるので、even=1 で初期化
even_count = 1
odd_count = 0

current_zeros = 0
ans = 0

for char in T:
    if char == '0':
        current_zeros += 1
        
    if current_zeros % 2 == 0:
        # 現在の0の数が偶数なら、過去の「偶数」の位置とペアを作れる
        ans += even_count
        even_count += 1
    else:
        # 現在の0の数が奇数なら、過去の「奇数」の位置とペアを作れる（奇数 - 奇数 = 偶数）
        ans += odd_count
        odd_count += 1
        
print(ans)
