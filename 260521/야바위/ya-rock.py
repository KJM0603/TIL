n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

ans = 0
for i in range(1,4):
    arr = ['X']*4 # 야바위 할 컵들
    arr[i] = 'O' # 각 위치별로 구슬 숨겨놓기
    cnt = 0 # 각 케이스별 점수

    for A,B,C in zip(a,b,c):
        arr[A],arr[B] = arr[B],arr[A] # 컵 위치 바꾸기
        if arr[C] == 'O': # 찍었는데 맞다면
            cnt += 1 # 점수 추가
    ans = max(ans,cnt) # 최고점 갱신

print(ans)