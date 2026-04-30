A = input()

# Please write your code here.
status = 'No'

for i in range(len(A)-1):
    if A[i] != A[i+1]:
        status = 'Yes'

print(status)