A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0

for i in range(0,A+1):
  for j in range(0,B+1):
    for k in range(0,C+1):
      if( (i * 500 + j * 100 + k * 50) == X):
        count = count + 1

print(count)    