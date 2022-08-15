N = int(input())
L = list(map(int, input().split()))

count = 0 
for i in range(0,N-2):
  for j in range(i + 1, N - 1):
    for k in range(j + 1, N):
      print(i)
      print(j)
      print(k)
# 1 , 2 , 3
# 1 , 2 , 4
# 1 , 2 , 5
# 1 , 3 , 4
# 1 , 3 , 5
# 1 , 4 , 5

# 2 , 3 , 4
# 2 , 3 , 5

