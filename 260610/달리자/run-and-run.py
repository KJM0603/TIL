n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

cnt = 0

for i in range(n-1,0,-1):
    for j in range(i-1,-1,-1):
        while A[j] >= 1 and A[i] < B[i]:
            A[j] -= 1
            A[i] += 1
            cnt += (i-j)

print(cnt)