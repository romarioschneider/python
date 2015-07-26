#!/usr/bin/env python3

import sys
import unicodedata

def print_unicode_table(words):
    print("decimal hex chr {0:^40}".format("name"))
    print("------- ----- --- {0:-<40}".format(""))
    
    code = ord(" ")
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        for i in words:
            if i in name.lower():
                check_in = True
            else:
                check_in = False
                break
        if words is None or check_in == True:
            print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
        code += 1
        
words = None
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [word1 | word2 word3 ...]".format(sys.argv[0]))
        word = 0
    else:
        words = list()
        i = 1
        while i < len(sys.argv):
            words.append(sys.argv[i].lower())
            i += 1
            
    if words != 0:
        print_unicode_table(words)