import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  S = input().strip()
  print(N)
  
  full = 2 ** N - 1
  mask = (1 << N) - 1
  print(mask)
  
  danger = []
  for i, d in enumerate(S, start=1):
    if d == '1':
      format_binary = format(i, 'b')
      # print(format_binary)
      danger_int = int(format_binary, 2)
      tmp = []
      for j, b in enumerate(reversed(format_binary), start=1):
        if b == '1':
          tmp.append(j)
      danger.append(tmp)
      
      full |= danger_int ^ mask
  print(danger)
  print(format(full, 'b'))