n = int(input())
ls = list(map(int, input().split()))
f = [1] * (n+1) # 以i结尾的递增子序列最长为f[i]
for i in range(1,n):
    for j in range(i):
        if ls[j]>ls[i]:
            f[j] = max(f[j],f[i]+1)

ans = max(f)