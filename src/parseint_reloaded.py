# parseInt() reloaded from CodeWars

import codewars_test as test

def clean(string):
    string = string.replace('-', ' ')
    string = string.replace(' and ', ' ')
    return  string

def to_numeral(string):
    string_split = string.split()
    for i in range(0, len(string_split)):
        string_split[i] = '0' if string_split[i] == 'zero' else string_split[i]
        string_split[i] = '1' if string_split[i] == 'one' else string_split[i]
        string_split[i] = '2' if string_split[i] == 'two' else string_split[i]
        string_split[i] = '3' if string_split[i] == 'three' else string_split[i]
        string_split[i] = '4' if string_split[i] == 'four' else string_split[i]
        string_split[i] = '5' if string_split[i] == 'five' else string_split[i]
        string_split[i] = '6' if string_split[i] == 'six' else string_split[i]
        string_split[i] = '7' if string_split[i] == 'seven' else string_split[i]
        string_split[i] = '8' if string_split[i] == 'eight' else string_split[i]
        string_split[i] = '9' if string_split[i] == 'nine' else string_split[i]
        string_split[i] = '10' if string_split[i] == 'ten' else string_split[i]
        string_split[i] = '11' if string_split[i] == 'eleven' else string_split[i]
        string_split[i] = '12' if string_split[i] == 'twelve' else string_split[i]
        string_split[i] = '13' if string_split[i] == 'thirteen' else string_split[i]
        string_split[i] = '14' if string_split[i] == 'fourteen' else string_split[i]
        string_split[i] = '15' if string_split[i] == 'fifteen' else string_split[i]
        string_split[i] = '16' if string_split[i] == 'sixteen' else string_split[i]
        string_split[i] = '17' if string_split[i] == 'seventeen' else string_split[i]
        string_split[i] = '18' if string_split[i] == 'eighteen' else string_split[i]
        string_split[i] = '19' if string_split[i] == 'nineteen' else string_split[i]
        string_split[i] = '20' if string_split[i] == 'twenty' else string_split[i]
        string_split[i] = '30' if string_split[i] == 'thirty' else string_split[i]
        string_split[i] = '40' if string_split[i] == 'forty' else string_split[i]
        string_split[i] = '50' if string_split[i] == 'fifty' else string_split[i]
        string_split[i] = '60' if string_split[i] == 'sixty' else string_split[i]
        string_split[i] = '70' if string_split[i] == 'seventy' else string_split[i]
        string_split[i] = '80' if string_split[i] == 'eighty' else string_split[i]
        string_split[i] = '90' if string_split[i] == 'ninety' else string_split[i]
        string_split[i] = '100' if string_split[i] == 'hundred' else string_split[i]
        string_split[i] = '1000' if string_split[i] == 'thousand' else string_split[i]
        string_split[i] = '1000000' if string_split[i] == 'million' else string_split[i]
    return ' '.join(string_split)

def below_1000(string):
    for i in string.split():
        if i == '100':
            index_of_100 = string.split().index('100')
            if index_of_100 != 0 and int(string.split()[index_of_100-1]) < 10:
                string_split = string.split()
                string_split[index_of_100] = str(int(string_split[index_of_100-1]) * 100)
                string_split[index_of_100-1] = '0'
                string = ' '.join(string_split)
    return sum(int(i) for i in string.split())

def parse_int(string):
    string = clean(string)
    string = to_numeral(string)
    if '1000' in string.split():
        for i in string.split():
            if i == '1000':
                # Substring from right of 1000
                sub_string_right = string.split()[string.split().index('1000')+1:]
                sub_string_right = below_1000(' '.join(sub_string_right))
                # Substring left of 1000
                sub_string_left = string.split()[:string.split().index('1000')]
                sub_string_left = below_1000(' '.join(sub_string_left))*1000
                out = sub_string_left + sub_string_right
    else:
        out = below_1000(string)
    if '1000000' in string.split():
        out = 1000000
    return out

# test.assert_equals(parse_int('one'), 1)
# test.assert_equals(parse_int('twenty'), 20)
# test.assert_equals(parse_int('sixty-eight'), 68)
# test.assert_equals(parse_int('two hundred forty-six'), 246)
# test.assert_equals(parse_int('one hundred'), 100)
# test.assert_equals(parse_int('one thousand'), 1000)
# test.assert_equals(parse_int('two thousand'), 2000)
# test.assert_equals(parse_int('two thousand two hundred forty-six'), 2246)
# test.assert_equals(parse_int('one hundred thousand'), 100000)
# test.assert_equals(parse_int('twenty six thousand three hundred fifty nine'), 26359)
test.assert_equals(parse_int('one million'), 1000000)

