from sortedcontainers import SortedList
import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

st = SortedList()
ans = 0

def nearest(x):
    i = st.bisect_left(x)
    res = 10**18

    if i > 0:
        res = min(res, x - st[i-1])
    if i < len(st) - 1:
        res = min(res, st[i+1] - x)

    return res

# 初回
st.add(0)
x = X[0]
st.add(x)
ans = 2 * x
print(ans)

for x in X[1:]:
    i = st.bisect_left(x)

    hit = []
    if i < len(st):
        hit.append(st[i])
    if i > 0:
        hit.append(st[i-1])

    for nx in hit:
        ans -= nearest(nx)

    st.add(x)

    hit.append(x)
    for nx in hit:
        ans += nearest(nx)

    print(ans)