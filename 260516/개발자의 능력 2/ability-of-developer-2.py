abilities = list(map(int, input().split()))

# Please write your code here.
ans = sum(abilities)

def div_team(cnt,left,right,left_cnt,right_cnt):
    global ans
    if cnt == 6:
        if left_cnt == 2 and right_cnt == 2:
            center = sum(abilities) - left - right
            check_list = [left,right,center]
            total = max(check_list) - min(check_list)
            ans = min(ans,total)
        return

    div_team(cnt+1,left+abilities[cnt],right, left_cnt+1, right_cnt)
    div_team(cnt+1, left, right+abilities[cnt], left_cnt, right_cnt+1)
    div_team(cnt+1,left,right, left_cnt, right_cnt)

div_team(0,0,0,0,0)
print(ans)