N,K,T = input().split()
str_list = []
for _ in range(int(N)):
    word = input()
    if word.startswith(T):
        str_list.append(word)

str_list = sorted(str_list)
ans = str_list[int(K)-1]
print(ans)