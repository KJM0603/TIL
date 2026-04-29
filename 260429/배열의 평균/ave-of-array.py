arr = [list(map(int,input().split())) for _ in range(2)]

arr_t = [list(x) for x in zip(*arr)]

for i in range(2):
    print(f'{sum(arr[i])/4:.1f}', end=' ')
print()
for j in range(4):
    print(f'{sum(arr_t[j])/2:.1f}', end=' ')
print()
total = 0
for i in range(2):
    for j in range(4):
        total += arr[i][j]

print(f'{total/8:.1f}')