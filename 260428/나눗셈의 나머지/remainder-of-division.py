A,B = map(int,input().split())

ans_list = [0]*B
while A >= B:
    w = A%B
    ans_list[w] += 1
    A //= B
ans_list[A] += 1
squared = list(map(lambda x: x**2, ans_list))
ans = sum(squared)
print(ans)