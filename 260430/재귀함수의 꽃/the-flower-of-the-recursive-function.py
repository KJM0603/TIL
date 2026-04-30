N = int(input())

# Please write your code here.
def recur(cnt,n):
    if cnt == N:
        return
    print(n,end=' ')
    recur(cnt+1,n-1)
    print(n,end=' ')

recur(0,N)