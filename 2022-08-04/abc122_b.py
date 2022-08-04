n = int(input())
S = input()

c = 0

for i in range(n-2):
    if(S[i:i+3] == "ABC"):
        c += 1

print(str(c))