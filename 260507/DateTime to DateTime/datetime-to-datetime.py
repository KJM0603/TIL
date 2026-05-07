a, b, c = map(int, input().split())

# Please write your code here.
ans = (a-11)*1440 + (b-11)*60 + (c-11)

if ans >= 0:
    print(ans)
else:
    print(-1)