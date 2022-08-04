A, B = map(int, input().split())

while(A >0 and B > 0):
    # point: n桁目を計算する
    if( ( A % 10 ) + (B % 10) >= 10 ):
        print("Hard")
        exit()
    # point: n桁目にずらす。切り捨て除算
    A //= 10
    B //= 10

print("Easy")