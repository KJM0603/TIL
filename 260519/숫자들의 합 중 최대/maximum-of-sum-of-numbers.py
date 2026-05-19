X, Y = map(int, input().split())

# Please write your code here.
ans = 0

for num in range(X,Y+1):
    num_str = str(num)
    list_str = list(map(int,(num_str)))
    total = sum(list_str)
    ans = max(ans,total)

print(ans)