ls = [1,2,2,2,3,4,5,5,5,6,6,7,8,10,18]
left,right = 0,len(ls)
target = 5

def binarySearch(l,r,target):
    while l<=r:
        mid = (l+r)//2
        if ls[mid] == target:
            return mid
        elif ls[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return -1

print(binarySearch(left,right-1,0))


# >=target的最小值
def binarySearch2(l,r,target):
    while l<r:
        mid = (l+r)>>2
        if ls[mid]>=target:
            r = mid
        else:
            l = mid+1
    return l
print(binarySearch2(left,right-1,-1))


# <= target 的最大值
def binarySearch3(l,r,target):
    while l<r:
        mid = (l+r+1)>>2
        if ls[mid]<=target:
            l = mid
        else:
            r = mid-1
    return l

print(binarySearch3(left,right-1,19))

# 求根号2

def get_sqrts(l,r,eps):
    while (r-l)>=eps:
        mid = (l+r)/2
        if mid*mid<2:
            l = mid
        else:
            r = mid
    return l
    
print(get_sqrts(1,2,0.01))

# 切木头
logs = [10,24,15]
k = 7
def cutLogs(l,r,k):
    while l<r:
        mid = (l+r)//2
        nums = 0
        for c in logs:
            nums+=c//mid
        if nums > k:
            l = mid+1
        else:
            r = mid
    return l
