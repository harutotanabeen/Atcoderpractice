A,B,K = map(int, input().split())
ans = []
for i in range(1,101):
    # 割り切れる
    if(A % i == 0 and B % i == 0):
        ans.append(i)
# K番目に大きい、後ろから数えてX番目
print(ans[-K])

#a,b,k = map(int,input().split())
#ans = []
#for i in range(1,101):
#    if a%i==0 and b%i==0:
#        ans.append(i)
#print(ans)
#print(ans[-k])