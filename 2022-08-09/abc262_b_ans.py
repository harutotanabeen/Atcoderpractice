N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]


for _ in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  A[u][v] = True
  A[v][u] = True
  print(A)