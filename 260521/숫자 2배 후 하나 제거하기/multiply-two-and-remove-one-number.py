n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
ans = sum(arr)
for i in range(n):
    arr[i] *= 2

    for j in range(n):
        total = 0
        num_list = []
        for k in range(n):
            if j==k:
                continue
            num_list.append(arr[k])
        for k in range(n-2):
            total += abs(num_list[k]-num_list[k+1])
        ans = min(ans,total)
    arr[i] //= 2

print(ans)