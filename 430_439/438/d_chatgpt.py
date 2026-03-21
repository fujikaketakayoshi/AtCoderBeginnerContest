import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

SA = [0]*(N+1)
SB = [0]*(N+1)
SC = [0]*(N+1)

for i in range(N):
    SA[i+1] = SA[i] + A[i]
    SB[i+1] = SB[i] + B[i]
    SC[i+1] = SC[i] + C[i]

ans = 0

# xは1以上、yはx+1以上、y<N
# なので y は 2 〜 N-1 (1-indexed)

best = SA[1] - SB[1]  # x=1 の場合

for y in range(2, N):
    # y固定で計算
    current = best + SB[y] + (SC[N] - SC[y])
    ans = max(ans, current)
    
    # 次の y のために x=y を候補に追加
    best = max(best, SA[y] - SB[y])

print(ans)
