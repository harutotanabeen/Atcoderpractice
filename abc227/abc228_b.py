n, x = map(int, input().split())
a = list(map(int, input().split()))
 
b = []

for _ in range(n):
    # 秘密を知った友達を追加
    b.append(x)
    # 次の秘密を知った友達を検索
    x = a[x - 1]
    print(x)

# 重複した列は数えない
print(len(set(b)))