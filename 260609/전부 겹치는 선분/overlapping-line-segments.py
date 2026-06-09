N = int(input())
arr = [0]*101
for _ in range(N):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        arr[i] += 1

status = 'No'

for i in range(len(arr)):
    if arr[i] == N:
        status = 'Yes'

print(status)