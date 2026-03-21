S = input().strip()
T = input().strip()

print(S.replace('A',''),T.replace('A',''))


if S.replace('A','') != T.replace('A',''):
    print(-1)
    exit()

def f(s):
    res = []
    cnt = 0
    for c in s:
        if c == 'A':
            cnt += 1
        else:
            res.append(cnt)
            cnt = 0
    res.append(cnt)
    return res

Sa = f(S)
Ta = f(T)

print(Sa, Ta)

print(sum(abs(x-y) for x,y in zip(Sa,Ta)))