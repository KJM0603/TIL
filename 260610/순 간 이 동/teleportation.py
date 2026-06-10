a, b, x, y = map(int, input().split())

# Please write your code here.

cases = []

cases.append(abs(a-b))
cases.append(abs(x-a) + abs(y-b))
cases.append(abs(a-y) +abs(x-b))

print(min(cases))