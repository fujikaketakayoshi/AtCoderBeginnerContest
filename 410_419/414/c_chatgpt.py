import sys
input = sys.stdin.readline

A = int(input())
N = int(input())
# print(A, N)

def base_n(num, base):
    if num == 0:
        return "0"

    s = ""
    while num:
        s = str(num % base) + s
        num //= base

    return s

ans = 0
for x in range(1, 1000000):
  s = str(x)
  odd_pal = int(s + s[-2::-1])
  if odd_pal <= N:
    odd_pala = base_n(odd_pal, A)
    if odd_pala == odd_pala[::-1]:
      ans += odd_pal
  
  even_pal = int(s + s[::-1])
  if even_pal <= N:
    even_pala = base_n(even_pal, A)
    if even_pala == even_pala[::-1]:
      ans += even_pal;

print(ans)