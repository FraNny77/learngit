n = int(input())
nums = list(map(int,input().split()))
N = 1000010
pre = [i for i in range(N)]
def find(x):
    r = x
    while r!=pre[r]:
        r=pre[r]
    while r!=x:
        j = pre[x]
        pre[x] = r
        x =j
    return r

for i in range(len(nums)):
    root = find(nums[i])
    nums[i] = root
    pre[root] = find(root+1)

print(*nums)

