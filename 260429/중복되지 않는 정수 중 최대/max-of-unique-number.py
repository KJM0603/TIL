n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
num_set = set()

for i in nums:
    if nums.count(i) == 1:
        num_set.add(i)

if num_set:
    ans = max(num_set)
else:
    ans = -1
print(ans)