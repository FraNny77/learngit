import math


# 朴素筛法
def isPrime(n):
    if n == 2:
        return 1
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i==0:
            return 0
    return 1


# 埃筛
def getPrimesAi(n):
    primes = []
    vis = [0 for i in range(n+10)]
    for i in range(2,n+1):
        if not vis[i]:
             primes.append(i)
        for j in range(i+i,n+1,i):
            vis[j] = 1
    return primes


# 线性筛
def getPrimes(n):
    minp = [0 for i in range(n+10)]
    primes = []
    vis = [0 for i in range(n+10)]
    for i in range(2,n+1):
        if not vis[i]:
            primes.append(i)
            minp[i] = i
        j = 0
        while i*primes[j] <=n:
            vis[i*primes[j]] = 1
            minp[i*primes[j]] = primes[j]
            if i%primes[j] ==0:break
            j+=1
    return primes