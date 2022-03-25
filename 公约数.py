# 最大公约数
import math


def gcb(a, b):
    if a == 0:
        return a
    return gcb(b, a % b)


# 最小公倍数
def mins(a, b):
    return a*b//gcb(a, b)


# n的质因数分解


def depart(n):
    dic = set()
    for i in range(2, int(n/i)+1):
        if i*i > n:
            break
        while n % i == 0:
            dic[i] = dic.get(i,0)+1
            n //= i
    if n > 1:
        print(n, 1)


def getPrimes(n):
    vis = [0 for i in range(n+10)]
    minp = [0 for i in range(n+10)]
    primes = []
    for i in range(2, n+1):
        if not vis[i]:
            primes.append(i)
            minp[i] = i
        j = 0
        while i*primes[j] <= n:
            minp[i*primes[j]] = primes[j]
            vis[i*primes[j]] = 1
            if i % primes[j] == 0:
                break
            j += 1
    return minp
# n!的质因数分解


def depatch(n):
    minp = getPrimes(n)
    dic = {}
    for i in range(2,n+1):
        curP = minp[i]
        while i%curP ==0:
            dic[curP]=dic.get(curP,0)+1
            i//=curP
    return dic
print(depatch(5))
