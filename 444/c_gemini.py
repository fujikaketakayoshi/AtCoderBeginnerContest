import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
A = list(map(int, input().split()))
A.sort()

def check(L):
    # L が A のどの要素よりも小さい場合はありえない
    if L < A[-1]:
        return False
    
    d = deque(A)
    while d:
        # 一番大きい要素が L そのものなら、1本で成立
        if d[-1] == L:
            d.pop()
        # そうでなければ、最小と最大を組み合わせて L になる必要がある
        elif len(d) >= 2 and d[0] + d[-1] == L:
            d.popleft()
            d.pop()
        else:
            return False
    return True

ans = set()

# 候補1: L が最大値と同じ
cand1 = A[-1]
if check(cand1):
    ans.add(cand1)
    
# 候補2: L が最大値 + 最小値
cand2 = A[0] + A[-1]
if check(cand2):
    ans.add(cand2)
    
print(*sorted(list(ans)))
