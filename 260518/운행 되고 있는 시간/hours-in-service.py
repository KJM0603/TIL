n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

arr = [0]*1001
ans = 0

for a,b in times:
    for time in range(a,b):
        arr[time] += 1

for a,b in times:
    cnt = 0
    for time in range(a,b):
        arr[time] -= 1
    for i in range(len(arr)):
        if arr[i] > 0:
            cnt += 1
    ans = max(ans,cnt)
    for time in range(a,b):
        arr[time] += 1

print(ans)