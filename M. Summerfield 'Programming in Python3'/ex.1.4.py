#!/usr/bin/env python3.4

import sys
import random

article = ("a", "the", "an")
noun = ("boy", "girl", "cat", "dog", "man", "woman")
verb = ("sang", "ran", "jumped", "shouted", "threw")
adverb = ("loudly", "quietly", "well", "badly")

if sys.argc > 1:
    try:
        
iterable = "12345"
for i in iterable:
    line = ""
    line = line + random.choice(article) + " " + random.choice(noun) + " " + random.choice(verb)
    if random.randint(0, 1) == 1:
        line = line + " " + random.choice(adverb)
    print(line)