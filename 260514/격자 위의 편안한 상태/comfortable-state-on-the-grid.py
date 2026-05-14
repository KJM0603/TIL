n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]
points = [(x-1,y-1) for x,y in points]
grid = [[0]*n for _ in range(n)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]
ans = 0
for r,c in points:
    grid[r][c] = 1
    cnt = 0
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] == 1:
                cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)