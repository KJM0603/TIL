n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.'
dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < n and 0<= ny < n:
                if grid[nx][ny] == 1:
                    cnt += 1
        if cnt >= 3:
            ans += 1

print(ans)