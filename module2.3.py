my_list = [42,69,0,322,13,0,99,-5,9,8,7,-6,5]
b = 0
while b < len(my_list):
    if my_list[b] > 0:
        print(my_list[b])
        b = b + 1
    elif my_list[b] == 0:
        b = b + 1
    else:
        break
