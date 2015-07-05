#!/usr/bin/env python3.4

import sys

zero = ("  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  ")
one = (" * ", "** ", " * ", " * ", " * ", " * ", "***")
two = (" *** ", "*   *", "*   *", "   * ", "  *  ", " *   ", "*****")
three = (" *** ", "*   *", "   * ", "  ** ", "   * ", "*   *", " *** ")
four = ("   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  ")
five = ("*****", "*    ", "*    ", " *** ", "    *", "    *", "**** ")
six = (" ****", "*    ", "*    ", "**** ", "*   *", "*   *", " *** ")
seven = ("*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    ")
eight = (" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** ")
nine = (" *** ", "*   *", "*   *", " ****", "    *", "    *", " *** ")

digits = (zero, one, two, three, four, five, six, seven, eight, nine)

try:
    row = 0
    digits_input = sys.argv[1]
    
    while row < len(zero):
        line = ""
        column = 0
        
        while column < len(digits_input):
            number = int(digits_input[column])
            digit = digits[number]
            
            for i in digit[row]:
                if i == "*":
                    line = line + str(number)
                else:
                    line = line + " "
                    
            line = line + "  "
            column += 1
            
        print(line)
        row += 1
except IndexError:
    print("Usage: ex.1.1.py <int number>")
except ValueError as err:
    print(err, "in", digits_input)