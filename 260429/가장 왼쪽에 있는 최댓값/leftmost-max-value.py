n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max_idx = len(a)

ans_list = []

while max_idx > 0:
    max_v = 0
    for i in range(0,max_idx):
        if max_v < a[i]:
            max_v = a[i]
            max_idx = i
    ans_list.append(max_idx+1)

print(*ans_list)