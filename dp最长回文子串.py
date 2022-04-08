s = input()
dp = [[0]*(len(s)+1) for i in range(len(s)+1)]
ans = 1
for i in range(len(s)):
    dp[i][i] = 1
    if i < len(s)-1:
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            ans = 2

for l in range(3, len(s)+1):  # 枚举子串的长度
    i = 0
    while i+l-1 < len(s):  # 枚举子串的起始端点
        j = i+l-1  # 子串的右端点 （len(substring)-1）
        if s[i] == s[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1
            ans = l
        i += 1
print(ans)
