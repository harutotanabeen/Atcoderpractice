n,a,b = map(int, input().split())

ans = []
for i in range(1,n+1):
    # 各桁の合計
    sum_d = 0
    num = i
    while num > 0:
        sum_d += num % 10
        num //= 10
    if(sum_d >= a and sum_d <= b):
        ans.append(i)

print(sum(ans))
