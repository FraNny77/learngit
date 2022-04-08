# cab = ca-1b + ca-1b-1
N =1010
mod = 1e9+7
c = [[0]*(N) for i in range(N)]
for i in range(N):
    for j in range(i+1):
        if j == 0:
            c[i][j] = 1
        else:
            c[i][j] = (c[i-1][j]+c[i-1][j-1])%mod


