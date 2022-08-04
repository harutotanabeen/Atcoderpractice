A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
N = int(input())
b = [int(input()) for i in range(N)]# ソートを行う
 
hit = list()

ans = "No"
for i in range(N):
        if b[i] == A[0]:
                hit.append(1)
        if b[i] == A[1]:
                hit.append(2)
        if b[i] == A[2]:
                hit.append(3)
        if b[i] == B[0]:
                hit.append(4)
        if b[i] == B[1]:
                hit.append(5)
        if b[i] == B[2]:
                hit.append(6)
        if b[i] == C[0]:
                hit.append(7)
        if b[i] == C[1]:
                hit.append(8)
        if b[i] == C[2]:
                hit.append(9)
 
dct = sorted(hit)
 
 
if 1 in dct:
        if 2 in dct:
                if 3 in dct:
                        ans = "Yes"
        if 4 in dct:
                if 7 in dct:
                        ans = "Yes"
        if 5 in dct:
                if 9 in dct:
                        ans = "Yes"
if 2 in dct:
        if 5 in dct:
                if 8 in dct:
                        ans = "Yes"
 
if 3 in dct:
        if 6 in dct:
                if 9 in dct:
                        ans = "Yes"
        if 5 in dct:
                if 7 in dct:
                        ans = "Yes"
 
if 4 in dct:
        if 5 in dct:
                if 6 in dct:
                        ans = "Yes"
 
if 7 in dct:
        if 8 in dct:
                if 9 in dct:
                        ans = "Yes"
 
print(ans)