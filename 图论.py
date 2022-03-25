import heapq
n, m, s, e = map(int, input().strip().split())
g = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().strip().split())
    g[a].append((b, c))
    # g[b].append((a,c))


def topSort():
    que = []
    ans = []
    n, m = map(int, input().strip().split())
    g = [[] for i in range(n+1)]
    ins = [0 for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().strip().split())
        ins[b] += 1
        g[a].append(b)
    for i in range(1, n+1):
        if ins[i] == 0:
            que.append(i)
    while que:
        t = que.pop(0)
        ans.append(t)
        for np in g[t]:
            ins[np]-=1
            if ins[np] == 0:
                que.append(np)
    if len(ans) == n:
        print(*ans)
    else:
        print("exist loop")



def dijkstra(s):
    # 单源最短路 用于无负边
    dist = [float('inf') for i in range(n+10)]
    dist[s] = 0
    que = []
    heapq.heappush(que, (0, s))
    while que:
        t = heapq.heappop(que)
        curDis = t[0]
        node = t[1]
        for np, w in g[node]:
            if dist[np] > curDis+w:
                dist[np] = curDis+w
                heapq.heappush(que, (dist[np], np))
    return dist[n]


def SPFA(s):
    # 多源最短路 解决负边 负环
    que = [s]
    st = [0 for i in range(n+10)]
    st[s] = 1
    dist = [float('inf') for i in range(n+10)]
    while que:
        t = que.pop(0)
        st[t] = 0
        for np, w in g[t]:
            if dist[np] > dist[t]+w:
                dist[np] = dist[t]+w
                if not st[np]:
                    que.append(np)
                    st[np] = 1
    return dist[n]


pre = [i for i in range(n+1)]


def find(x):
    r = x
    while pre[r] != r:
        r = pre[r]
    while x != r:
        j = pre[x]
        pre[x] = r
        x = j
    return r


def kruskal():
    cnt = 0
    res = 0
    n, m = map(int, input().strip().split())
    edges = []
    for i in range(m):
        a, b, c = map(int, input().strip().split())
        edges.append((a, b, c))
    edges.sort(key=lambda x: x[2])
    for i in range(m):
        a, b, c = edges[i]
        fa, fb = find(a), find(b)
        if fa != fb:
            pre[fa] = fb
            cnt += 1
    if cnt < n-1:
        print(-1)
    else:
        print(res)
