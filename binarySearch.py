ls = list(range(1, 11))
l, r = 0, len(ls)
target = 10
import bisect
idx = bisect.bisect(ls,target)

def binarySearch(l, r, target):
    while l <= r:
        mid = (l+r)//2
        if ls[mid] == target:
            return mid
        elif ls[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return -1


# 最小>=target
def binarySearch2(l, r, target):
    while l < r:
        mid = (l+r)//2
        if ls[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l

# 最大<=target


def binarySeach3(l, r, target):
    while l < r:
        mid = (l+r+1)//2
        if ls[mid] <= target:
            l = mid
        else:
            r = mid-1
    return l


# 2的平方根
def get_sqrt(l, r, eps):
    while r-l > eps:
        mid = (l+r)/2
        if mid*mid < 2:
            l = mid
        else:
            r = mid
    return mid


print(get_sqrt(1, 2, 0.0001))


# 截木棒
logs = [100, 50, 30]


def cut(l, r, logs):
    res = -1
    while l <= r:
        mid = (l+r)//2
        cnt = 0
        for i in logs:
            cnt += i//mid
            

