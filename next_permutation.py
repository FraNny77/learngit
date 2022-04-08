n = int(input())
idx = int(input())
ls = list(map(int,input().split()))


def next_permutation(idx):
    for t in range(idx):
        if n<=1:
            return
        for i in range(n-2,-1,-1): # 从后往前看
            if ls[i] < ls[i+1]: # 找到第一个不是降序的数x
                for j in range(n-1,-1,-1): # 从后往前找 找到第一个大于x的数
                    if ls[j]>ls[i]:  # 将他们交换
                        ls[i],ls[j] = ls[j],ls[i]
                        ls[i+1:] = sorted(ls[i+1:])  # 后面的数按升序排列
                        break
                break
            else:
                if i==0:
                    ls.sort()


def pre_permutation(idx):
    for t in range(idx):
        if n<=1:
            return 
        for i in range(n-2,-1,-1):
            if ls[i] > ls[i+1]:
                for j in range(n-1,-1,-1):
                    if ls[j]<ls[i]:
                        ls[i],ls[j] = ls[j],ls[i]
                        ls[i+1:] = sorted(ls[i+1:],reverse=True)
                        break
                break
            else:
                if i==0:
                    ls = sorted(ls,reverse=True)