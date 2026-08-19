import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# 鳩 i がいる内部箱
pigeon = list(range(N + 1))

# 巣番号 i が対応している内部箱
nest = list(range(N + 1))

# 内部箱 i が現在何番の巣として見えるか
label = list(range(N + 1))

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        _, a, b = query
        pigeon[a] = nest[b]

    elif query[0] == 2:
        _, a, b = query

        box_a = nest[a]
        box_b = nest[b]

        nest[a], nest[b] = box_b, box_a
        label[box_a], label[box_b] = b, a

    else:
        _, a = query
        print(label[pigeon[a]])