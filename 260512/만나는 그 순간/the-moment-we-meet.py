n, m = map(int, input().split())

time_list_n = [0]*1000000
now = 0
num = 0
for _ in range(n):
    direction, time = input().split()
    time = int(time)
    if direction == 'R':
        for t in range(time):
            now += 1
            num += 1
            time_list_n[now] = num
    else:
        for t in range(time):
            now += 1
            num -= 1
            time_list_n[now] = num

time_list_m = [0]*1000000
now = 0
num = 0
for _ in range(m):
    direction, time = input().split()
    time = int(time)
    if direction == 'R':
        for t in range(time):
            now += 1
            num += 1
            time_list_m[now] = num
    else:
        for t in range(time):
            now += 1
            num -= 1
            time_list_m[now] = num

ans = -1
for i in range(1,now):
    if time_list_n[i] == time_list_m[i] and time_list_m[i-1] != time_list_n[i-1]:
        ans = i
        break

print(ans)