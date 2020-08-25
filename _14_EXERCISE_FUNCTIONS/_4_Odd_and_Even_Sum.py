def odd_even_sum_str(text):
    sum_even = 0
    sum_odd = 0

    for ch in text:
        num = int(ch)
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    # print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


number = input()
res = odd_even_sum_str(number)

print(res)
