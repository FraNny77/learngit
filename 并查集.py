n, m = map(int, input().strip().split())
relations = []
for i in range(m):
    a, b = map(int, input().strip().split())
    relations.append((a, b))


def find(x):
    r = x
    while r != pre[r]:
        r = pre[r]
    while x != r:
        j = pre[x]
        pre[x] = r
        x = j
    return r


def union(a, b):
    fa, fb = find(a), find(b)
    if fa != fb:
        pre[fa] = fb


pre = [i for i in range(n+1)]
