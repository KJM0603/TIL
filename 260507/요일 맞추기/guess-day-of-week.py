m1, d1, m2, d2 = map(int, input().split())

cnt = 0
end_of_day = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
}
if m1 == m2:
    cnt += (d2-d1)
    
if m1 < m2:
    while m1 != m2:
        d1 += 1
        cnt += 1
        if end_of_day[m1] == d1:
            m1 += 1
            d1 = 1
            cnt += 1
    cnt += (d2-1)

if m1 > m2:
    while m1 != m2:
        d2 += 1
        cnt -= 1
        if end_of_day[m2] == d2:
            m2 += 1
            d2 = 1
            cnt -= 1
    cnt -= (d1 - 1)


if cnt%7 == 0:
    print('Mon')
elif cnt%7 == 1:
    print('Tue')
elif cnt%7 == 2:
    print('Wed')
elif cnt%7 == 3:
    print('Thu')
elif cnt%7 == 4:
    print('Fri')
elif cnt%7 == 5:
    print('Sat')
elif cnt%7 == 6:
    print('Sun')