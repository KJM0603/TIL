N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr = sorted(arr)

# 최솟값을 += 1` (최댓값은 최솟값 +k)
# arr을 순회하며 최댓값 안에 있는 숫자까지 카운트
# 이 카운트 값이 최댓값인지 체크

ans = 0
for min_v in range(1,10000):
    cnt = 0
    for i in range(N):
        if min_v <= arr[i] <= min_v+K:
            cnt += 1
    ans = max(ans,cnt)

print(ans)