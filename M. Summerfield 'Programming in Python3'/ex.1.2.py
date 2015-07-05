#!/usr/bin/env python3.4

numbers_list = []
sum = 0
i = 0
try:
    while True:
        try:
            numbers_list.append(float(input("enter a number or Enter to finish:")))
            sum = sum + numbers_list[i]
            i += 1
        except ValueError:
            break
        except EOFError:
            break

    lowest = numbers_list[0]
    for i in numbers_list:
        if i < lowest:
            lowest = i
    higest = numbers_list[0]
    for i in numbers_list:
        if i > higest:
            higest = i
    mean = sum / len(numbers_list)
    print("numbers:", numbers_list)
    print("count =", len(numbers_list), "sum =", sum, "lowest =", lowest, "higest =", higest, "mean = ", mean)
except IndexError as err:
        print(err)