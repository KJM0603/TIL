n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
max_v = 0
for i in range(n):
    if arr[i] > t:
        cnt += 1
    else:
        if max_v < cnt:
            max_v = cnt
        cnt = 0
if max_v < cnt:
    max_v = cnt

print(max_v)