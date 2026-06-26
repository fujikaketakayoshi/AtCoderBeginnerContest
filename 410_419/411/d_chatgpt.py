import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# node0 = 空文字列
parent = [-1]
add = ['']

pc = [0] * N
server = 0

for _ in range(Q):
    query = input().split()
    t = int(query[0])

    if t == 1:
        p = int(query[1]) - 1
        pc[p] = server

    elif t == 2:
        p = int(query[1]) - 1
        s = query[2]

        parent.append(pc[p])
        add.append(s)
        pc[p] = len(parent) - 1

    else:
        p = int(query[1]) - 1
        server = pc[p]
print(pc)
print(add)
print(parent)
print(server)

ans = []
cur = server

while cur != 0:
    ans.append(add[cur])
    cur = parent[cur]

ans.reverse()
print(''.join(ans))