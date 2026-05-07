n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0]*201

offset = 100

for a,b in segments:
    arr[a+offset:b+offset] = [x+1 for x in arr[a+offset:b+offset]]

print(max(arr))