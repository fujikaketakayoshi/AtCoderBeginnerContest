from collections import deque
import sys
input = sys.stdin.readline

Q = int(input())

q = deque()

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        c, x = query[1], query[2]
        q.append((x, c))

    else:
        k = query[1]
        ans = 0

        while k > 0:
            x, c = q.popleft()

            if c >= k:
                ans += x * k
                c -= k

                if c > 0:
                    q.appendleft((x, c))

                k = 0

            else:
                ans += x * c
                k -= c

        print(ans)