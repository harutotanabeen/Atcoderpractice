S = input()

if S[0] == S[1] and S[1] == S[2] and S[0] == S[2]:
    print(1)
    exit()

if S[0] != S[1] and S[1] != S[2] and S[0] != S[2]:
    print(6)
    exit()

print(3)

