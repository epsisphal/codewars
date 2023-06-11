# Replace with alphabet position from CodeWars

import codewars_test as test
from random import randint

def alphabet_position(text):
    text = text.replace(" ", "").lower()
    out = ""
    for character in text:
        if ord(character) -96 > 0:
            out += str(ord(character) - 96) + " "
    return(out[:-1])

# Solution
# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
test.assert_equals(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

number_test = ""
for item in range(10):
    number_test += str(randint(1, 9))
test.assert_equals(alphabet_position(number_test), "")

# print(alphabet_position("The sunset sets at twelve o' clock."))
