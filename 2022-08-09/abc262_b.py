n, m = map(int, input().split())
adj = [[False] * n for _ in range(n)]
for _ in range(m):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  adj[u][v] = True
  adj[v][u] = True

print(adj)