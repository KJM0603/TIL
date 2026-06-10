X = int(input())

# Please write your code here.

num = 0
cnt = 0

for i in range(1,150):
    if num+i <= X:
        num += i
        cnt += 1

        if num+i <= X:
            num += i
            cnt += 1
        else:
            break
    else:
        break

if num < X:
    cnt += 1

print(cnt)