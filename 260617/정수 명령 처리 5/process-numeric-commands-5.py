N = int(input())

lst = []
for _ in range(N):
    line = input().split()

    if line[0] == 'push_back':
        lst.append(line[1])
    elif line[0] == 'pop_back':
        lst.pop()
    elif line[0] == 'get':
        print(lst[int(line[1])-1])
    else:
        print(len(lst))