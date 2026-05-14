N = int(input())
arr = list(map(int, input().split()))

min_v = max(arr)*len(arr)*len(arr)
for i in range(N):
    total = 0
    for j in range(N):
        total += arr[j]*abs(j-i)
    min_v = min(min_v, total)

print(min_v)