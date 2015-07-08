#!/usr/bin/env python3.4

import sys
import random

article = ("a", "the", "an")
noun = ("boy", "girl", "cat", "dog", "man", "woman")
verb = ("sang", "ran", "jumped", "shouted", "threw")
adverb = ("loudly", "quietly", "well", "badly")

try:
    if 0 <= int(sys.argv[1]) <= 10:
        iterable = int(sys.argv[1])
    else:
        iterable = 5
except IndexError:
    iterable = 5
except ValueError:
    print("Need int number. Default = 5")
    iterable = 5
        
i = 0        
while i < iterable:
    line = ""
    line = line + random.choice(article) + " " + random.choice(noun) + " " + random.choice(verb)
    if random.randint(0, 1) == 1:
        line = line + " " + random.choice(adverb)
    print(line)
    i += 1