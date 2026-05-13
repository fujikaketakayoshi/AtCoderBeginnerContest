import sys
input = sys.stdin.readline
import heapq
from collections import deque

N, K = map(int, input().split())
# 客の情報: (到着時刻, 滞在時間, 人数, 元のインデックス)
groups = []
for i in range(N):
    a, b, c = map(int, input().split())
    groups.append((a, b, c, i))

groups = deque(groups)
# 店内で食べている客を管理する最小ヒープ: (退店時刻, 人数)
eating_heap = []
# 待ち行列: (到着時刻, 滞在時間, 人数, 元のインデックス)
waiting_q = deque()

ans = [0] * N
current_occupancy = 0

# 全員の入店時間が決まるまでループ
while groups or waiting_q:
    # 次に起こる「イベント時刻」を特定する
    # 1. 次の団体が到着する時刻
    next_arrival = groups[0][0] if groups else float('inf')
    # 2. 店内の誰かが食べ終わる時刻
    next_departure = eating_heap[0][0] if eating_heap else float('inf')
    
    # 現在時刻を、次に何かが起きる時刻まで進める
    now = min(next_arrival, next_departure)
    
    # --- 退店処理 ---
    # 今の時刻に退店する人がいれば全員出す
    while eating_heap and eating_heap[0][0] <= now:
        _, c_out = heapq.heappop(eating_heap)
        current_occupancy -= c_out
        
    # --- 到着処理 ---
    # 今の時刻に到着する人がいれば待ち行列へ
    while groups and groups[0][0] <= now:
        waiting_q.append(groups.popleft())
        
    # --- 入店判定 (ここが重要) ---
    # 待ち行列の先頭が店に入れる限り、どんどん入れる
    while waiting_q:
        a_i, b_i, c_i, original_idx = waiting_q[0]
        if current_occupancy + c_i <= K:
            waiting_q.popleft()
            ans[original_idx] = now
            current_occupancy += c_i
            # 退店時刻を計算してヒープに追加
            heapq.heappush(eating_heap, (now + b_i, c_i))
        else:
            # 先頭が入れないなら、後ろも待たせる
            break
            
print('\n'.join(map(str, ans)))
