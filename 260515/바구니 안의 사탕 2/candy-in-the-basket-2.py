N, K = map(int, input().split())
arr = [0]*501
offset = 200

for _ in range(N):
    count,idx = map(int,input().split())
    arr[idx+offset] += count

ans = 0
for i in range(200,501):
    total = sum(arr[i-K:i+K+1])
    ans = max(ans,total)

print(ans)