import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
S = input().strip()

# b < B の区間数
def count_b_less_than_B():
    l = 0
    cntb = 0
    res = 0
    for r in range(N):
        if S[r] == 'b':
            cntb += 1
        while cntb >= B:
            if S[l] == 'b':
                cntb -= 1
            l += 1
        res += (r - l + 1)
    return res

# a < A かつ b < B
def count_a_less_and_b_less():
    l = 0
    cnta = 0
    cntb = 0
    res = 0
    for r in range(N):
        if S[r] == 'a':
            cnta += 1
        else:
            cntb += 1
        
        while cntb >= B:
            if S[l] == 'a':
                cnta -= 1
            else:
                cntb -= 1
            l += 1
        
        while cnta >= A:
            if S[l] == 'a':
                cnta -= 1
            else:
                cntb -= 1
            l += 1
        
        res += (r - l + 1)
    return res

print(count_b_less_than_B() - count_a_less_and_b_less())