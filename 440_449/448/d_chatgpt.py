import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

g = [[] for _ in range(N)]

for _ in range(N-1):
    u,v = map(int,input().split())
    u-=1
    v-=1
    g[u].append(v)
    g[v].append(u)

from collections import defaultdict

cnt = defaultdict(int)
ans = [False]*N

def dfs(u,parent,dup):
    if cnt[A[u]] >= 1:
        dup = True

    cnt[A[u]] += 1

    ans[u] = dup

    for v in g[u]:
        if v==parent:
            continue
        dfs(v,u,dup)

    cnt[A[u]] -= 1

dfs(0,-1,False)

for x in ans:
    print("Yes" if x else "No")