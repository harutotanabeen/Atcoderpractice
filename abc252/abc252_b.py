N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 最大ものを探す
max = max(A)

maxlist = []

# 最大のもの順番特定
for i in range(N):
    if max == A[i]:
        maxlist.append(i+1)

# B列とマッチするとアウト
for j in range(K):
    if B[j] in maxlist:
        print('Yes')
        exit()

print('No')