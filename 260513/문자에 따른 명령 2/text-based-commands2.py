dirs = input()

# Please write your code here.
x = 0
y = 0
dir_num = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for dir in dirs:
    if 'L' in dir:
        dir_num = (dir_num-1)%4
    if 'R' in dir:
        dir_num = (dir_num+1)%4
    if 'F' in dir:
        x += dx[dir_num]
        y += dy[dir_num]

print(y,x)