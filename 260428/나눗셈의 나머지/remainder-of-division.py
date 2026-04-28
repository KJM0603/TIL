A,B = map(int,input().split())

ans_list = [0]*B
while A > 1:
    w = A%B
    ans_list[w] += 1
    A //= B
squared = list(map(lambda x: x**2, ans_list))
ans = sum(squared)
print(ans)