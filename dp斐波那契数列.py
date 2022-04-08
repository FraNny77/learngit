def fibnaci1(n):
    if n==1 or n==2 :return 1
    return fibnaci1(n-1)+fibnaci1(n-2)

N =1010
f = [0]*(N)
f[1] = 1
f[2] = 1
def fibnaci2(n):
    if f[n] !=0:
        return f[n]
    f[n] = fibnaci2(n-1)+fibnaci2(n-2)
    return f[n]

def fibnaci3(n):
    f = [0]*(n+1)
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]