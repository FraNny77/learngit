# 朴素01背包
n,m = map(int,input().split()) # n件物品 背包容量为m
w = [0]*(n+1)
v = [0]*(n+1)
for i in range(1,1+n):
    weight,val = map(int,input().split())
    w[i] = weight
    v[i] = val

dp = [[0]*(m+1) for i in range(n+1)]
for i in range(1,1+n):
    for j in range(m+1):
        dp[i][j] = dp[i-1][j]
        if j>=w[i]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])

# 滚动数组空间优化

f = [0]*(m+1)
for i in range(1,n+1):
    for j in range(m,-1,-1):
        if j>=w[i]:
            f[j] = max(f[j],f[j-w[i]]+v[i])
        

# 完全背包 （每件物品可以选择多次）

for i in range(1,1+n):
    for j in range(m+1): 
        dp[i][j] = dp[i-1][j]
        if j>=w[i]:
            dp[i][j] = max(dp[i][j],dp[i][j-w[i]]+v[i])

for i in range(1,n+1):
    for j in range(w[i],m+1):
        f[j] = max(f[j],f[j-w[i]]+v[i])

# 多重背包 第i件物品有nums[i]件
n,m = map(int,input().split())
N = 1010
w = [0]*(N)
v = [0]*(N)
f = [0]*(m+1)
cnt = 0
for i in range(1,n+1):
    weight,val,nums = map(int,input().split())
    k = 1
    while k<nums:
        cnt+=1
        w[cnt] = k*weight
        v[cnt] = k*val
        nums-=k
        k*=2
    if nums>0:
        cnt+=1
        w[cnt] = nums*weight
        v[cnt] = nums*val
        
for i in range(1,cnt+1):
    for j in range(m,w[i]-1,-1):
        f[j] = max(f[j],f[j-w[i]]+v[i])


# 分组背包
N = 1010
n,m = map(int,input().split())
s = [0]*(N)
w = [[0]*(N) for i in range(N)]
v = [[0]*(N) for i in range(N)]
f = [0]*(m+1)
for i in range(1,n+1):
    s[i] = int(input())
    for j in range(s[i]): # 第i组有s[i]件东西
        w[i][j] ,v[i][j] = map(int,input().split())

for i in range(1,n+1):
    for j in range(m,-1,-1):
        for k in range(s[i]):
            if j>=w[i][k]:
                f[j] = max(f[j],f[j-w[i][k]]+v[i][k])
print(f[m])