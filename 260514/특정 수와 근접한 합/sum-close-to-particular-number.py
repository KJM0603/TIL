N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
total = sum(arr)
ans = abs((total - arr[0] - arr[1])-S)
for i in range(N-1):
    for j in range(i+1,N):
        T = total - arr[i] - arr[j]
        possible = abs(T-S)
        ans = min(possible,ans)

print(ans)