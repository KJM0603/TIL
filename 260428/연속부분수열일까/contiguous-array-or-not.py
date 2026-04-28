N1, N2 = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

status = 'No'

for idx in range(len(A)):
    if A[idx] == B[0]:
        if A[idx:idx+len(B)] == B:
            status = 'Yes'

print(status)