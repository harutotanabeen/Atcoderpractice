n = int(input())
s = input()

a = []
# S の i 桁目を消す
for i in range(0,n):
    # 特定の文字を除外
    a.append(s[:i] + s[i+1:])

print(a)
# 重複削除してカウントして出力
print(len(set(a)))

