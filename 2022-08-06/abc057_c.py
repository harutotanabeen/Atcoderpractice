from functools import lru_cache

@lru_cache(maxsize=1000)
def memo(n,i):
    # 割り切れるi
    if(n % i == 0):
        # 割った数b
        b = int(n / i)
        # 桁数
        al = len(str(i))
        bl = len(str(b))
        # F(A,B)で大きい方
        if(al > bl):
           ans.append(al)
        else:
           ans.append(bl)

n = int(input())

# 半分まで計算
half = int((n+1)/2)
ans = []

for i in range(1,half+1):
    memo(n,i)


print(min(ans))