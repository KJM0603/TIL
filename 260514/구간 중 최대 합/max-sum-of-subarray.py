N,K = map(int, input().split())
arr = list(map(int, input().split()))

max_v = 0

for i in range(N-K+1):
    total = sum(arr[i:i+K])
    max_v = max(max_v,total)

print(max_v)