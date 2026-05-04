m1, d1, m2, d2 = map(int, input().split())

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cnt = 1

if m1 < m2 or (m1 == m2 and d1 < d2):
    now = [m1,d1]
    while now != [m2,d2]:
        if now[1] == num_of_days[now[0]]:
            now[0] += 1
            now[1] = 1
            cnt += 1
        cnt += 1
        now[1] += 1
    print(cnt)

else:
    now = [m2, d2]
    while now != [m1, d1]:
        if now[1] == num_of_days[now[0]]:
            now[0] += 1
            now[1] = 1
            cnt += 1
        cnt += 1
        now[1] += 1
    print(cnt)