n = int(input())
f = [[0]*(n+1) for i in range(n+1)]
f[1][1] = 1
for i in range(1,n+1):
    f[i][1] = 1
    f[i][i] = 1

for i in range(3,n+1):
    for j in range(2,i):
        f[i][j] = f[i-1][j]+f[i-1][j-1]

for i in range(1,n+1):
    for j in range(1,i+1):
        print(f[i][j],end=" ")
    print()