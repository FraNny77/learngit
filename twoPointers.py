ls = list(range(1,11))
k = 7
i,j = 0,len(ls)-1
while i<j:
    if ls[i]+ls[j] == k:
        print(i,j)
        break
    elif ls[i]+ls[j] <k:
        i+=1
    else:
        j-=1
    