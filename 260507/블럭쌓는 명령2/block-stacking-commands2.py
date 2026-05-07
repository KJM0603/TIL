N,K = map(int,input().split())
arr = [0]*(N+1)
for _ in range(K):
    a,b = map(int,input().split())
    arr[a:b+1] = [x+1 for x in arr[a:b+1]]

print(max(arr))