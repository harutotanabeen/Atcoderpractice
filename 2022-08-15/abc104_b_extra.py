S = input()

#  ポイントでないで考える
#  大文字のCを含む　→　大文字Cが1つしかない
#  それ以外が小文字 →　大文字はA,Cの2つしかない
if S[0] == 'A' and S[2:-1].count('C') == 1 and sum(map(str.isupper,S)) == 2:
  print("AC")
else:
  print("WA")
