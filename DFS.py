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
path = [-1 for i in range(n+10)]


def dfs(pos):
    # 找路径
    map[pos[0]][pos[1]] = 1
    if pos == (x1, y1):
        return 1
    for x, y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 < x <= n and 0 < y <= m and map[x][y] != '0':
            dfs((x, y))
            if (x, y) == (x1, y1):
                return 1
            if dfs((x, y)):
                print((x, y))
                return 1
            # map[x][y] = 0 找多种方案时要回溯
    return 0


def dfs_stack(start, end):
    stack = [(start, 0)]
    x, y = start
    map[x][y] = 1
    while stack:
        pos, num = stack.pop()
        for i in range(num, 4):
            x, y = pos[0]+dir[i][0], pos[1]+dir[i][1]
            if (x, y) == end:
                print(x, y)
                print(*stack)
                return
            if 0 < x <= n and 0 < y <= m and map[x][y] != 1:
                stack.append((x, y), 0)
                stack.append((start, i+1))
                map[x][y] = 1
                break
