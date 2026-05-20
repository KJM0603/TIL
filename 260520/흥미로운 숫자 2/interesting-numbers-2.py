X, Y = map(int, input().split())

def interesting(num):
    global cnt
    num_str = str(num)
    num_list = list(num_str)
    a_num = num_list[0]
    b_num = num_list[0]
    a_cnt = 0
    b_cnt = 0
    if num_list.count(a_num) == len(num_list):
        return

    for n in range(len(num_list)):
        if num_list[n] != a_num:
            b_num = num_list[n]
            break

    for n in range(len(num_list)):
        if a_cnt >= 2 and b_cnt >= 2:
            return
        if num_list[n] != a_num and num_list[n] != b_num:
            return
        if num_list[n] == a_num:
            a_cnt += 1
        if num_list[n] == b_num:
            b_cnt += 1
    if a_cnt >= 2 and b_cnt >= 2:
        return
    cnt += 1

cnt = 0
for i in range(X,Y+1):
    interesting(i)

print(cnt)