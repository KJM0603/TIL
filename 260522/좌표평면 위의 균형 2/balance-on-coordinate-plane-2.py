n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = n
for x in range(0,99,2):
    for y in range(0,99,2):
        quad_1 = 0
        quad_2 = 0
        quad_3 = 0
        quad_4 = 0
        for i,j in points:
            if i < x and j < y:
                quad_3 += 1
            elif i < x and j > y:
                quad_4 += 1
            elif i > x and j < y:
                quad_2 += 1
            else:
                quad_1 += 1
        candidate = max(quad_1,quad_2,quad_3,quad_4)
        ans = min(ans,candidate)

print(ans)