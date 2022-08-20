N = int(input())
S = input()

ans = ''

for i in range(0,len(S)):
  # 次の文字
  nchar = ord(S[i]) + N
  # Z移行なら引く
  if nchar >= 91:
    nchar = nchar - 26
  ans = ans + chr(nchar)

print(ans)  
