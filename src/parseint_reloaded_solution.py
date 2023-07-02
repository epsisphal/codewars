# Parse Int reloaded solution fromm CodeWars

import codewars_test as test

ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
        'eighteen', 'nineteen']
TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def parse_int(string):
    # print(string)
    numbers = []
    for token in string.replace('-', ' ').split(' '):
        if token in ONES:
            numbers.append(ONES.index(token))
        elif token in TENS:
            numbers.append((TENS.index(token) + 2) * 10)
        elif token == 'hundred':
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers = [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    return sum(numbers)

# test.assert_equals(parse_int('one'), 1)
# test.assert_equals(parse_int('twenty'), 20)
# test.assert_equals(parse_int('sixty-eight'), 68)
# test.assert_equals(parse_int('two hundred forty-six'), 246)
# test.assert_equals(parse_int('one hundred'), 100)
# test.assert_equals(parse_int('one thousand'), 1000)
# test.assert_equals(parse_int('two thousand'), 2000)
# test.assert_equals(parse_int('two thousand two hundred forty-six'), 2246)
# test.assert_equals(parse_int('one hundred thousand'), 100000)
test.assert_equals(parse_int('twenty six thousand three hundred fifty nine'), 26359)
# test.assert_equals(parse_int('one million'), 1000000)
