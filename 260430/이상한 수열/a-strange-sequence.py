N = int(input())

# Please write your code here.

num_list = [1,2]
ans = 0

def arr(idx):
    global ans

    if len(num_list) >= N:
        ans = num_list[N-1]
        return

    num = num_list[int((idx+1)/3)-1] + num_list[idx-1]
    num_list.append(num)
    arr(idx+1)

arr(2)
print(ans)