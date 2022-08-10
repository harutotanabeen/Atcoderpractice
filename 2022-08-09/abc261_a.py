l1,r1,l2,r2 = map(int, input().split())

count = 0
for i in range(0,101):
  if i >= l1 and i <= r1 and i >= l2 and i <= r2 and r1 != l2:
    count = count + 1

print(count)