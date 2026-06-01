N,M = map(int,input().split())
list_list = []
for _ in range(M):
    my_lst = sorted(list(map(int,(input().split()))))
    list_list.append(my_lst)

ans = 0

for i in range(M):
    candi = list_list.count(list_list[i])
    ans = max(ans,candi)

print(ans)