n = int(input())
commands = []
for _ in range(n):
    xi, di = input().split()
    commands.append((int(xi),di))

arr = [0]*2001

now = 1000

for num,command in commands:
    if command == 'R':
        arr[now:now+num] = [x+1 for x in arr[now:now+num]]
        now += num
    elif command == 'L':
        arr[now-num:now] = [x+1 for x in arr[now-num:now]]
        now -= num

cnt = 0

for i in arr:
    if i >= 2:
        cnt += 1

print(cnt)