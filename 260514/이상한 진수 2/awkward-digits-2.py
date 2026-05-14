a = input()
a = [x for x in a]
max_v = 0

for bin in range(len(a)):
    if a[bin] == '1':
        a[bin] = '0'
        bin_num = ''.join(a)
        ten_num = int(bin_num, 2)
        max_v = max(max_v,ten_num)
        a[bin] = '1'
    else:
        a[bin] = '1'
        bin_num = ''.join(a)
        ten_num = int(bin_num, 2)
        max_v = max(max_v, ten_num)
        a[bin] = '0'

print(max_v)