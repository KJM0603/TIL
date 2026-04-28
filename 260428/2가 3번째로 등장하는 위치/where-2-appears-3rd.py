N = int(input())
arr = list(map(int,input().split()))

cnt = 0
ans = 0
for idx in range(len(arr)):
    if arr[idx] == 2:
        cnt += 1
    if cnt == 3:
        ans = idx+1
        break

print(ans)