n = int(input())

# Please write your code here.
def square(n):
    arr = [[0]*n for _ in range(n)]

    num = 1
    for i in range(n):
        for j in range(n):
            arr[i][j] = num
            num += 1
            if num == 10:
                num = 1
    return arr

ans = square(n)
for row in ans:
    print(*row)