A, B, C = map(int, input().split())

# Please write your code here.
ans = 0
for i in range(1000):
    for j in range(1000):
        total = A*i + B*j
        if total > C:
            continue
        ans = max(ans,total)
print(ans)