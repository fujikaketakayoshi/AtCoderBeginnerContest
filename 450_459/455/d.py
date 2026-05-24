import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

deck_nums = [None] + [1 for _ in range(1, N + 1)]
card_next = [[None]] + [[0, 0] for _ in range(1, N + 1)]
card_index = [None] + [i for i in range(1, N + 1)]
# print(deck_nums)
# print(card_next)
# print(card_index)

for _ in range(Q):
  C, P = map(int, input().split())
  next_c = C
  pre_index = card_index[C]
  card_num = 1
  card_index[next_c] = card_index[P]
  card_next[card_index[next_c]][1] = 0
  next_index = card_index[P]
  while card_next[next_c][0] != 0:
    next_c = card_next[next_c][0]
    card_index[next_c] = card_index[P]
    card_num += 1
  print(C, P)
  deck_nums[pre_index] -= card_num
  deck_nums[next_index] += card_num
  card_next[C][1] = P
  card_next[P][0] = C
  print(card_next)
  print(card_index)
  print(deck_nums)

print(*deck_nums[1:])