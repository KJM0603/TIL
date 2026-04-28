N,Q = map(int,input().split())
arr = list(map(int,input().split()))
commands = [list(map(int,input().split())) for _ in range(N)]
for command in commands:
    if command[0] == 1:
        print(arr[command[1]-1])
    elif command[0] == 2:
        for i in range(len(arr)):
            if arr[i] == command[1]:
                print(i+1)
                break
        else:
            print(0)
    elif command[0] == 3:
        print(*arr[command[1]-1:command[2]])