one,two = map(int,input().split())

num_list = []
num_list.append(one)
num_list.append(two)

for i in range(8):
    three = two + 2*one
    num_list.append(three)
    one = two
    two = three

print(*num_list)