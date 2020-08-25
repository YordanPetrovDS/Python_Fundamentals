def is_palindrome(num_str):
    length = len(num_str)
    is_pln = True
    sum_ = length // 2

    for i in range(length // 2):
        if num_str[i] != num_str[length - 1 - i]:
            is_pln = False
            break

    return is_pln


nums = input().split(", ")
for num in nums:
    print(is_palindrome(num))
