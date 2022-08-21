import math

p = int(input())

ans = 0

# ポイント：for 文を逆から回す。一番上から引く
for i in range(10,0,-1):
    # 100枚使えるか確認
    for j in range(0,100):
        # 10を使うだけ使う
        # 階上をPで表す
        a = math.factorial(i)
        if p >= a:
            p = p - a
            ans = ans + 1

print(ans)
