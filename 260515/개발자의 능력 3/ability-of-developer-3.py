abilities = list(map(int, input().split()))

# Please write your code here.
ans = sum(abilities)

def div_team(cnt,left,left_cnt):
    global ans
    if cnt == 6:
        if left_cnt == 3:
            right = sum(abilities) - left
            total = abs(left-right)
            ans = min(ans,total)
        return

    div_team(cnt+1,left+abilities[cnt],left_cnt+1)
    div_team(cnt+1,left,left_cnt)

div_team(0,0,0)
print(ans)