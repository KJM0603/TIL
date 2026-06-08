x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.

status = 'overlapping'

if a1 > x2 or a2 < x1 or b1 > y2 or b2 < y1:
    status = 'nonoverlapping'

print(status)