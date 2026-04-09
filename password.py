N,M = map(int,input().split())
my_dict = {}
for _ in range(N):
    txt = input().split()
    my_dict[txt[0]] = txt[1]

for _ in range(M):
    key = input()
    print(my_dict[key])