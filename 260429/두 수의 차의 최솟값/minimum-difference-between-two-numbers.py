N = int(input())
arr = list(map(int,input().split()))

num_set = set()
for i in range(len(arr)-1):
    num_set.add(abs(arr[i]-arr[i+1]))

ans = min(num_set)
print(ans)