commands = []
for _ in range(3):
    cough,temp = input().split()
    commands.append((cough,int(temp)))

ans = [0]*4

for i,j in commands:
    if i == 'Y' and j >= 37:
        ans[0] +=1
    elif i == 'N' and j >= 37:
        ans[1] += 1
    elif i == 'Y' and j < 37:
        ans[2] += 1
    else:
        ans[3] += 1

if ans[0] >= 2:
    ans.append('E')

print(*ans)