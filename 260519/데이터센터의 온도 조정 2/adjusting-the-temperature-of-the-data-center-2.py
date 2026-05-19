N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
ans = 0
for i in range(1001):
    total = 0
    for a,b in ranges:
        if i < a:
            total += C
        elif a <= i <= b:
            total += G
        else:
            total += H
    ans = max(ans,total)

print(ans)