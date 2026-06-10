N = int(input())

loc = [-1]*11
count = [-1]*11

for _ in range(N):
    num,direction = map(int,input().split())
    if loc[num] != direction:
        count[num] += 1
    loc[num] = direction

ans = 0

for cnt in count:
    if cnt >= 1:
        ans += cnt

print(ans)