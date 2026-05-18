n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [x[0] for x in lines]
x2 = [x[1] for x in lines]

is_true = [True]*n

for i in range(n-1):
    for j in range(i+1,n):
        if (x1[i] < x1[j] and x2[i] > x2[j]) or (x1[i] > x1[j] and x2[i] < x2[j]):
            is_true[i] = False
            is_true[j] = False


print(is_true.count(True))