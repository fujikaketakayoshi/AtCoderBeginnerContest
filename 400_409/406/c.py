import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
print(N, P)

st1 = False
st2 = False

i = 1
ans = 0
pre = 0
suf = 0
while i < N - 1:
  if P[i - 1] < P[i] > P[i + 1]:
    ans += suf
    suf = 0
    st1 = True
    st2 = False
  elif P[i - 1] > P[i] < P[i + 1]:
    st2 = True
  
  if st1 == False and st2 == False:
    pre += 1
  elif st1 == True and st2 == True and i < N - 2 and P[i + 1] < P[i + 2]:
    suf += 1
  elif st1 == True and st2 == True and i < N - 2 and P[i + 1] > P[i + 2]:
    ans += 1
    st1 = False
    st2 = False
    ans += pre
    pre = 0
    i += 1
  elif i == N - 2 and st1 == True and st2 == True:
    ans += 1
    ans += pre + suf
  print(i, pre, suf, st1, st2)
  i += 1
print(ans)

