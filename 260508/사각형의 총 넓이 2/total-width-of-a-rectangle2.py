n = int(input())
arr = [[0]*201 for _ in range(201)]
offset = 100
for _ in range(n):
    x1,y1,x2,y2 = map(int, input().split())

    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[offset+i][offset+j] = 1

cnt = 0
for row in arr:
    cnt += row.count(1)

print(cnt)