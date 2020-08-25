def perfect_number(number):
    sum_ = 0
    for i in range(1, number):
        if sum_ > number:
            break
        else:
            if number % i == 0:
                sum_ += i
    if sum_ == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num = int(input())
perfect_number(num)
