S = input()

isOk = False
# ポイント：特定の文字を削除
for i in range(len(S)):
    # 一文字目がAではない
    if i == 1 and S[i] == 'A':
        isOk = True
        continue
    else:
        isOk = False
        print("WA")
        exit()
    if ( i >= 2 and i <= len(S)-2) and  S[i] in 'C':
        isOk = True
    elif S[i].islower:
        isOk = True
    else:
        print("WA")
        exit()