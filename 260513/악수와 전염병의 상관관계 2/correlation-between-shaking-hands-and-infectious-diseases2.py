N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]
handshakes = sorted(handshakes, key=lambda x: x[0]) # 시간 순 정렬

plague = [0]*(N+1) # 감염 여부
plague_count = [K]*(N+1) # 감염 시킬 수 있는 횟수
plague[P] = 1 # 최초 감염자

for t,x,y in handshakes:
    if plague[x] == 1 and plague[y] == 1:
        if plague_count[x] > 0:
            plague_count[x] -= 1
        if plague_count[y] > 0:
            plague_count[y] -= 1

    elif plague[x] == 1 and plague[y] == 0:
        if plague_count[x] > 0:
            plague_count[x] -= 1
            plague[y] = 1

    elif plague[x] == 0 and plague[y] == 1:
        if plague_count[y] > 0:
            plague_count[y] -= 1
            plague[x] = 1
    else:
        continue

ans = plague[1:]
print(''.join(map(str,ans)))