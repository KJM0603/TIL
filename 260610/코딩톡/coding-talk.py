n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]
participants = [chr(alphabet) for alphabet in range(65,65+n)]

read = set()
for i in range(p-1,m):
    read.add(c[i])

for j in range(p-1,0,-1):
    if u[j] == u[j-1]:
        read.add(c[j-1])
    else:
        break

ans = set()

for participant in participants:
    if participant not in read:
        ans.add(participant)

if u[p-1] == 0:
    ans = ''
ans = sorted(ans)
print(*ans)