import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  A = list(map(int, input().split()))
  # print(N, A)
  def_tonari = set()
  for i in range(2 * N - 1):
    if A[i] == A[i + 1]:
      def_tonari.add(A[i])
  # print(def_tonari)
  
  tonari_cnt = [[] for _ in range(N + 1)]
  
  if not A[0] in def_tonari:
    tonari_cnt[A[0]].append(set([A[1]]))
  for i in range(1, 2 * N - 1):
    if not A[i] in def_tonari:
      tonari_cnt[A[i]].append(set([A[i - 1], A[i + 1]]))
  if not A[-1] in def_tonari:
    tonari_cnt[A[-1]].append(set([A[-2]]))
  
  # print(tonari_cnt)
  
  ans = set()
  for a, t in enumerate(tonari_cnt):
    if t:
      # print(t[0], t[1], t[0] & t[1])
      for b in t[0] & t[1]:
        ans.add(tuple(sorted((a, b))))
  
  print(len(ans))

