import sys
input = sys.stdin.readline

S = input().strip()
a, b, c = 0, 0, 0
for i in S:
    if i == "A":
        a += 1
    if i == "B":
        b = min(a, b + 1)
    if i == "C":
        c = min(b, c + 1)
print(c)
