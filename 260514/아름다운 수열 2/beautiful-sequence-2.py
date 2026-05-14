N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B = sorted(B)

cnt = 0
for i in range(N-M+1):
    isit_B = sorted(A[i:i+M])
    if isit_B == B:
        cnt += 1

print(cnt)