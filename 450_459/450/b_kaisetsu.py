import sys
input = sys.stdin.readline

N=int(input())
C=[[None]*(i+1)+list(map(int,input().split())) for i in range(N-1)]
print(C)
for a in range(N):
    for b in range(a+1,N):
        for c in range(b+1,N):
            if C[a][b]+C[b][c]<C[a][c]:
                print("Yes")
                break
        else:
            continue
        break
    else:
        continue
    break
else:
    print("No")
