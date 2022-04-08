# 求组合数Cab
# Cab = Ca-1b + Ca-1b-1
N = 2010
mod = 1e9+7
c = [[0]*N for j in range(N)]


def gen():
    for i in range(N):
        for j in range(i+1):
            if j == 0:
                c[i][j] = 1
            else:
                c[i][j] = (c[i-1][j]+c[i-1][j-1]) % mod


n = int(input())
gen()
for k in range(n):
    a, b = map(int, input().split())
    print(c[a][b])
