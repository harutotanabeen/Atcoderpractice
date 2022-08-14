h,n = map(int, input().split())


if h % n == 0:
  print(h // n)
else:
  print(h // n  + 1)

