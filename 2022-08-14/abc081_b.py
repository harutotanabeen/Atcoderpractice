n = int(input())
a = list(map(int, input().split()))

flag = True
counter = 0

# ポイント１：whileで繰り返す
while flag:
  for i in range(0,n):
    # 2で割れるかチェック
    if a[i] % 2 == 0:
      a[i] = a[i] // 2
    # 2で割れないなら終わり
    else:
      print(counter)
      exit()
  # ポイント２：for文の外で足す1すればOK
  counter = counter + 1

print(counter)