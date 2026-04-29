N = int(input())
arr = [[0]*N for _ in range(N)]

num = 1
for i in range(N-1,-1,-1):
    for j in range(N-1,-1,-1):
        if i%2 == (N-1)%2:
            arr[j][i] = num
            num += 1
        else:
            arr[N-1-j][i] = num
            num += 1

for row in arr:
    print(*row)