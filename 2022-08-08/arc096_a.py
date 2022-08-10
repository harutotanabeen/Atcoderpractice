A,B,C,X,Y = map(int, input().split())

ans = []
# ABあり
if X>Y:
    mx=int(X*2)
else:
    mx=int(Y*2)

# ABなし
ans.append(A*X+B*Y)

# 2つ飛ばし
for i in range(2,mx,2):
    half = i / 2
    # AB消化
    if half > X and half > Y:
        ans.append(int(C * i))
    elif half > X:
        ans.append(int(C * i) + B * (Y - half) )
    elif half > Y:
        ans.append(int(C * i) + A * (X - half) )
    else:
        # AB両方消化
        ans.append(int(A * (X - half) + B * (Y - half) + C * i))

print(min(ans))
