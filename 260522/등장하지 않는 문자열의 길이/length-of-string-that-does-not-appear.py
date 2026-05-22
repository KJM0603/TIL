N = int(input())
str = input()

# Please write your code here.

cnt = 1
def str_len(length):
    global cnt

    if length == N: # 끝까지 온 경우
        return

    found = False # flag

    for i in range(N+1-length):
        for j in range(i+1,N+1-length):
            if str[i:i+length] == str[j:j+length]:
                found = True
                break
        if found:
            break

    if not found:
        return

    cnt += 1

    str_len(length+1)

str_len(1)
print(cnt)