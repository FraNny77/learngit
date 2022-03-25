a,k,m = map(int,input().strip().split())
def qpow(a,k,m):
    res = 1
    while k:
        if k&1:
            res = res*a%m
        k>>=1
        a=a*a%m
    return res