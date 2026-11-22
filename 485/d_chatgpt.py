import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

# 左側の最短ABC
pre = set()
l = 0
while l < N and len(pre) < 3:
    pre.add(S[l])
    l += 1

# 右側の最短ABC
suf = set()
r = N - 1
while r >= 0 and len(suf) < 3:
    suf.add(S[r])
    r -= 1


print(l, r)
# 中央部分だけを尺取り法で処理
cnt = {'A': 0, 'B': 0, 'C': 0}
right = l
ans = 0

for left in range(l, r + 1):

    # ABCが揃うまで右端を伸ばす
    while right <= r and min(cnt.values()) == 0:
        cnt[S[right]] += 1
        right += 1

    if min(cnt.values()) == 0:
        break

    # rightは中央区間の終端の1つ先
    ans += r - right + 2

    # 次のleftへ
    cnt[S[left]] -= 1

print(ans)