import sys
input = sys.stdin.readline

SKY = 2000
N = int(input())

grid = [[0]*(SKY+2) for _ in range(SKY+2)]
clouds = []

# ① いもす
for _ in range(N):
    U,D,L,R = map(int,input().split())
    clouds.append((U,D,L,R))
    grid[U][L] += 1
    grid[D+1][L] -= 1
    grid[U][R+1] -= 1
    grid[D+1][R+1] += 1

# ② 横方向累積
for r in range(1, SKY+1):
    for c in range(1, SKY+1):
        grid[r][c] += grid[r][c-1]

# ③ 縦方向累積
for c in range(1, SKY+1):
    for r in range(1, SKY+1):
        grid[r][c] += grid[r-1][c]

one = [[0]*(SKY+2) for _ in range(SKY+2)]
for r in range(1, SKY+1):
    for c in range(1, SKY+1):
        if grid[r][c] == 1:
            one[r][c] = 1
for r in range(1, SKY+1):
    for c in range(1, SKY+1):
        one[r][c] += one[r-1][c]
        one[r][c] += one[r][c-1]
        one[r][c] -= one[r-1][c-1]

total_covered = 0
for r in range(1, SKY+1):
    for c in range(1, SKY+1):
        if grid[r][c] > 0:
            total_covered += 1

for i in range(N):
  U, D, L, R = clouds[i]
  unique = (
    one[D][R]
    - one[U-1][R]
    - one[D][L-1]
    + one[U-1][L-1]
  )
  print(SKY * SKY - (total_covered - unique))

