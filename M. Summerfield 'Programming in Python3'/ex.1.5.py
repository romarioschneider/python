#!/usr/bin/env python3.4

#as per conditions we must not use list.sort() and x % 2

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
    print("numbers: ", numbers_list)
    sorted_list = []
    i = 0
    numbers_list_l = len(numbers_list)
    position = 0
    while  numbers_list_l > 0:
        min = numbers_list[i]
        
        n = i
        while n < len(numbers_list):
            if numbers_list[n] <= min:
                min = numbers_list[n]
                position = n
            n = n + 1
            
        numbers_list.pop(position)   
        sorted_list.append(min)
        numbers_list_l = numbers_list_l - 1
        
    if ((len(sorted_list) / 2) != (len(sorted_list) // 2)):
        median = sorted_list[len(sorted_list) // 2]
    else:
        median = (sorted_list[len(sorted_list) // 2] + sorted_list[len(sorted_list) // 2 - 1]) / 2
    print(sorted_list)   
    print("count =", len(sorted_list), "sum =", sum, "lowest =", lowest, "higest =", higest, "mean =", mean, "median =", median)
except IndexError:
        print("Not received any number")