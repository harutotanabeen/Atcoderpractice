import math

p = int(input())

flag = True
coin = 1
ans = 0

while flag:
    # 金額を引く
    ans = p - math.factorial(coin)
    # 支払いOKならループ抜ける
    if ans <= 0 :
        flag = False
    coin = coin + 1

print(coin)



