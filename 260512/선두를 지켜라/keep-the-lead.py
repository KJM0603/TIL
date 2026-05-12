N, M = map(int, input().split())

arr_n = [0]*1000000
now_n = 0
num_n = 1
for _ in range(N):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        now_n += 1
        arr_n[now_n] = arr_n[now_n-1] + num_n*vi

arr_m = [0]*1000000
now_m = 0
num_m = 1
for _ in range(M):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        now_m += 1
        arr_m[now_m] = arr_m[now_m-1] + num_m*vi


total_time = now_n
leader = 0
cnt = 0
for i in range(total_time+1):
    if leader == 'N':
        if arr_n[i] < arr_m[i]:
            leader = 'M'
            cnt += 1
    elif leader == 'M':
        if arr_n[i] > arr_m[i]:
            leader = 'N'
            cnt += 1
    else:
        if arr_n[i] < arr_m[i]:
            leader = 'M'
        elif arr_n[i] > arr_m[i]:
            leader = 'N'
            
print(cnt)