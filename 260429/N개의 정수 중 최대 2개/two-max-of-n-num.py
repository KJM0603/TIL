n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
ans_list = sorted(a)
print(ans_list[-1],ans_list[-2])