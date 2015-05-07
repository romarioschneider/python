import _thread
import time

def conditions (s_number, length):
    if s_number.count("1") == 6 and s_number.count("2") == 3 and s_number.count("3") == 4:
        i = 0
        while i < length - 1:
            if s_number[i] == "3" and s_number[i + 1] == "3":
                n = -1
                break
            else:
                n = 0
            i = i + 1
    else:
        n = -1

    return int(n)

def progress_band(start, stop, length):
    
    n_numbers = 0
    while start < stop:

        if conditions(str(start), length) == 0:
            n_numbers = n_numbers + 1

        start = start + 1

    print (n_numbers)

length = 13
_thread.start_new_thread(progress_band, (1111112223333, 1666639695278, length))
_thread.start_new_thread(progress_band, (1666639695278, 2222167167222, length))
_thread.start_new_thread(progress_band, (2222167167222, 2777694639167, length))
_thread.start_new_thread(progress_band, (2777694639167, 3333222111111, length))

time.sleep(900000)