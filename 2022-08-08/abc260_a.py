s = input()

# 一度ソートする
a = sorted(s)

if a[0] == a[1] and a[1] == a[2]:
    print("-1")
elif a[0] == a[1]:
    print(a[2])
elif a[1] == a[2]:
    print(a[0])
else:
    print(a[0])
