S = input()

isOk = False
# ポイント：特定の文字を削除
for i in range(len(S)):
    # 一文字目がAではない
    if S[i] in 'A':
        print("A")
    else:
    # 一文字目がAではない
    if ( i >= 2 and i <= len(S)-2) and  S[i] in 'C':
        print("C")
