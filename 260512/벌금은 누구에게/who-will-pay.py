N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
life = [K]*N
ans = -1
for punish in student:
    life[punish-1] -= 1
    if life[punish-1] == 0:
        ans = punish
        break

print(ans)