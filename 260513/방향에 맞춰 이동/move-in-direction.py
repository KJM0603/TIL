n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dirs = [move[0] for move in moves]
dists = [int(move[1]) for move in moves]

# Please write your code here.
x = 0
y = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for dir,dist in zip(dirs,dists):
    if dir == 'N':
        x += dx[1]*dist
        y += dy[1]*dist
    elif dir == 'E':
        x += dx[0]*dist
        y += dy[0]*dist
    elif dir == 'S':
        x += dx[3]*dist
        y += dy[3]*dist
    elif dir == 'W':
        x += dx[2]*dist
        y += dy[2]*dist

print(y,x)