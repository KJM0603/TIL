X, Y = map(int, input().split())

# Please write your code here.
cnt = 0
for num in range(X,Y+1):
    num = str(num)
    num_list = list(num)
    pel_num_list = num_list[::-1]
    if num_list == pel_num_list:
        cnt += 1
print(cnt)