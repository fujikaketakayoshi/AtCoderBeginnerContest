import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

maxA = max(A)

# 長さごとの個数
freq = [0] * (maxA + 2)
for a in A:
    freq[a] += 1

print(freq)

# Ai >= j の個数を作る（後ろから累積）
cnt = [0] * (maxA + 2)
s = 0
for i in range(maxA, 0, -1):
    s += freq[i]
    cnt[i] = s
print(cnt)


# 筆算
carry = 0
ans = []

for i in range(1, maxA + 1):
    print(i, carry)
    total = cnt[i] + carry
    ans.append(str(total % 10))
    carry = total // 10

# 残りの carry
while carry > 0:
    ans.append(str(carry % 10))
    carry //= 10

print(''.join(ans[::-1]))
