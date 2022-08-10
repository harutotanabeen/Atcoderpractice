A,B,C,X,Y = map(int, input().split())

# ABを買わないパターン　入力例２
ans1 = A*X + B*Y

# ABを最大で買うパターン　入力例１
# 大きい方の2倍の価格＋あまった価格
if X > Y:
    ans2 = C*Y*2 + A*(X - Y)
else:
    ans2 = C*X*2 + B*(Y - X)

# ABだけで買うパターン（2倍して買う）入力例３
max_xy = max(X,Y)
ans3 = C*max_xy*2

print(min(ans1,ans2,ans3))