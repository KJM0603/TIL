N = int(input())
arr = list(map(int,input().split()))
num_list = []

for i in range(N):
    num_list.append(arr[i])
    if i%2 == 0:
        num_list = sorted(num_list)
        print(num_list[i//2] ,end=' ')