s,t = list(map(int, input().split()))

ans = 0

# ポイント：Sが最大値になる、rangeは+1しないとだめ
for a in range(0,s+1):
    for b in range(0,s+1):
        for c in range(0,s+1):
            if (a + b + c) <= s and a * b * c <= t:
                ans = ans + 1

print(ans)