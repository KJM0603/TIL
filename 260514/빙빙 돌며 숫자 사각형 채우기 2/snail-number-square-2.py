n, m = map(int, input().split())
grid = [[0]*m for _ in range(n)]

direction = 0
r = 0
c = 0
dr = [1,0,-1,0]
dc = [0,1,0,-1]
num = 1

while num <= n*m:
    grid[r][c] = num
    if num == n*m:
        break
    nr = r + dr[direction]
    nc = c + dc[direction]

    if 0 <= nr < n and 0<= nc < m and grid[nr][nc] == 0:
        num += 1
        r = nr
        c = nc

    else:
        direction = (direction+1)%4

for row in grid:
    print(*row)