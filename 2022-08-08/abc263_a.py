A,B,C,D,E = map(int, input().split())

a = []

a.append(A)
a.append(B)
a.append(C)
a.append(D)
a.append(E)

for i in range(1,14):
    if a.count(i) == 3:
        print('Yes')
        exit()

print('No')