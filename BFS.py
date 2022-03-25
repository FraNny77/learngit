from collections import deque
n, m = map(int, input().strip().split())
x0, y0, x1, y1 = map(int, input().strip().split())
map = [[0 for i in range(m+2)] for j in range(n+2)]
for i in range(m+2):
    map[0][i] = 1
    map[-1][i] = 1
for i in range(n+2):
    map[i][0] = 1
    map[i][-1] = 1
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def BFS(start, end):
    que = deque()
    que.append((start,0))
    while que:
        pos,cnt = que.popleft()
        map[pos[0]][pos[1]] = 1
        for i in range(4):
            np = pos[0]+dirs[i][0],pos[1]+dirs[i][1]
            if np==end:
                print(cnt)
                return
            if 0 < np[0] <= n and 0 < np[1] <= m and map[np[0]][np[1]] != 1:
                que.append((np,cnt+1))
    
        