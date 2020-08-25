n = int(input())

for i in range(1, n + 1):
    new_num = str(i)
    sum_num = 0
    for k in new_num:
        sum_num += int(k)
    is_special = sum_num in [5, 7, 11]
    print(f"{i} -> {is_special}")
    # if sum_num == 5 or sum_num == 7 or sum_num == 11:
    #     print(f"{i} -> True")
    # else:
    #     print(f"{i} -> False")
