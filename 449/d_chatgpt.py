import sys
input=sys.stdin.readline

L,R,D,U=map(int,input().split())

def f(k):
    x=max(0, min(R,k)-max(L,-k)+1)
    y=max(0, min(U,k)-max(D,-k)+1)
    print(k,x,y)
    return x*y

K=max(abs(L),abs(R),abs(D),abs(U))

ans=0
prev=0

for k in range(0,K+1):
    cur=f(k)
    if k%2==0:
        ans+=cur-prev
    prev=cur

print(ans)