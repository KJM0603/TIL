n, m = map(int, input().split())
# Process robot A's movements
now_a = 0
num_a = 0
arr_a = [0]*2000000
for _ in range(n):
    time, direction = input().split()
    if direction == 'L':
        for _ in range(int(time)):
            now_a += 1
            num_a -= 1
            arr_a[now_a] = num_a
    else:
        for _ in range(int(time)):
            now_a += 1
            num_a += 1
            arr_a[now_a] = num_a
for i in range(now_a,len(arr_a)):
    arr_a[i] = num_a

# Process robot B's movements
now_b = 0
num_b = 0
arr_b = [0]*2000000
for _ in range(m):
    time, direction = input().split()
    if direction == 'L':
        for _ in range(int(time)):
            now_b += 1
            num_b -= 1
            arr_b[now_b] = num_b
    else:
        for _ in range(int(time)):
            now_b += 1
            num_b += 1
            arr_b[now_b] = num_b
for i in range(now_b,len(arr_b)):
    arr_b[i] = num_b

cnt = 0
total_time = 0

if now_a >= now_b:
    total_time = now_a
else:
    total_time = now_b

for k in range(1,total_time):
    if arr_a[k] == arr_b[k] and arr_a[k-1] != arr_b[k-1]:
        cnt += 1

print(cnt)