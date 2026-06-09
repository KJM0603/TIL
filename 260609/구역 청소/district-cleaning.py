a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.

answer = 0

if a <= c <= b <= d:
    answer = d - a
elif a < b <= c < d:
    answer = (b-a) + (d-c)
elif a <= c < d <= b:
    answer = b - a
elif c <= a <= d <= b:
    answer = b - c
elif c < d <= a < b:
    answer = (d-c) + (b-a)
elif c <= a < b <= d:
    answer = d - c

print(answer)