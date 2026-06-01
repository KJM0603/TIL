n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.

status = 0
num = 1
while True:
    mul_num = num*2
    cnt = 0
    for a,b in ranges:
        if mul_num < a or mul_num > b:
            break
        else:
            mul_num *= 2
            cnt += 1
    if cnt == n:
        print(num)
        status = 1
        break
    num += 1