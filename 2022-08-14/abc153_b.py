h,n = map(int, input().split())
a = list(map(int, input().split()))

t = sum(a)
if h <= t:
  print("Yes")
else:
  print("No")
