n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
max_v = 0
cnt = 1

for i in range(1,n):
    if arr[i-1] == arr[i]:
        cnt += 1
    else:
        if max_v < cnt:
            max_v = cnt
        cnt = 1
if max_v < cnt:
    max_v = cnt

print(max_v)