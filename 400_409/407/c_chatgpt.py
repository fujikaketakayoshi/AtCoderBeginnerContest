import sys
input = sys.stdin.readline

S = input().strip()

btnB = 0
for c in reversed(S):
    btnB += (int(c) - btnB % 10 + 10) % 10

print(len(S) + btnB)