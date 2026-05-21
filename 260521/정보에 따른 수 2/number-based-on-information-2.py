T, a, b = map(int, input().split())
arr = [0]*1001

for _ in range(T):
    char, pos = input().split()
    arr[int(pos)] = char

cnt = 0
for i in range(a,b+1):
    for j in range(1000):
        if i-j >= 0 and i+j <= 1000:
            if arr[i-j] == 'S' or arr[i+j] == 'S':
                cnt += 1
                break
            elif arr[i-j] == 'N' or arr[i+j] == 'N':
                break

print(cnt)