n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
ans = max(x) * max(y)

for i in range(n):
    x_copy = [p[0] for p in points]
    y_copy = [p[1] for p in points]
    x_copy.pop(i)
    y_copy.pop(i)

    rect = (max(x_copy)-min(x_copy)) * (max(y_copy)-min(y_copy))
    ans = min(ans,rect)

print(ans)