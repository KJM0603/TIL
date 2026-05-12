x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.

arr = [[0]*2001 for _ in range(2001)]
offset = 1000
x1 = [x+1000 for x in x1]
x2 = [x+1000 for x in x2]
y1 = [x+1000 for x in y1]
y2 = [x+1000 for x in y2]

for i in range(2):
    for j in range(x1[i],x2[i]):
        for k in range(y1[i],y2[i]):
            arr[j][k] = 1

for j in range(x1[2],x2[2]):
    for k in range(y1[2],y2[2]):
        arr[j][k] = 0

cnt = 0
for j in range(2001):
    for k in range(2001):
        if arr[j][k] == 1:
            cnt += 1

print(cnt)