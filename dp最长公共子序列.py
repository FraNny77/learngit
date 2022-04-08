n = int(input())
s1 = input()
s2 = input()
dp = [[0]*(n+1) for i in range(n+1)]
for i in range(1,1+n):
    for j in range(1,1+n):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

ans = dp[n][n]