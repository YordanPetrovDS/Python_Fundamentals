def loading_bar(number):
    percentage = str(number) + "% [" + "%" * int(number / 10) + "." * abs(int(number / 10) - 10) + "]"

    if number != 100:
        print(percentage)
        print("Still loading...")
    else:
        print("100% Complete!")
        print("[%%%%%%%%%%]")


num = int(input())
loading_bar(num)
