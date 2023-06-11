# Decode the Morse code from CodeWars
import codewars_test as test

# from preloaded import MORSE_CODE

# import MORSE_CODE

def MORSE_CODE(string):
    return 'A'

def decode_morse(morse_code):
    out = ''
    for word in morse_code.strip().split('   '):
        for letter in word.split(' '):
            out += MORSE_CODE[letter]
        out += ' '
    return out.strip()

def decode_morse_copilot(morse_code):
    return ' '.join(''.join(MORSE_CODE(i) for i in word.split(' ')) for word in morse_code.strip().split('   '))

# @test.describe("Fixed tests")
# def tests():
        
#     @test.it("Should obtain correct decoding of Morse code from the description")
#     def test_morse_hey_jude():
#         test.assert_equals(decode_morse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

#     @test.it("Should obtain correct decoding of Morse code for basic examples")
#     def test_morse_basic_examples():
#         test.assert_equals(decode_morse('.-'), 'A')
#         test.assert_equals(decode_morse('--...'), '7')
#         test.assert_equals(decode_morse('...-..-'), '$')
#         test.assert_equals(decode_morse('.'), 'E')
#         test.assert_equals(decode_morse('..'), 'I')
#         test.assert_equals(decode_morse('. .'), 'EE')
#         test.assert_equals(decode_morse('.   .'), 'E E')
#         test.assert_equals(decode_morse('...-..- ...-..- ...-..-'), '$$$')
#         test.assert_equals(decode_morse('----- .---- ..--- ---.. ----.'), '01289')
#         test.assert_equals(decode_morse('.-... ---...   -..-. --...'), '&: /7')
#         test.assert_equals(decode_morse('...---...'), 'SOS')
#         test.assert_equals(decode_morse('... --- ...'), 'SOS')
#         test.assert_equals(decode_morse('...   ---   ...'), 'S O S')
        
#     @test.it("Should obtain correct decoding of Morse code for examples with extra spaces")
#     def test_morse_basic_examples_with_extra_spaces():
#         test.assert_equals(decode_morse(' . '), 'E')
#         test.assert_equals(decode_morse('   .   . '), 'E E')

#     @test.it("Should obtain correct decoding of Morse code for a complex example, and should ignore leading and trailing whitespace")
#     def test_morse_complex_example():
#         test.assert_equals(decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '), 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')

print(decode_morse('.   . .'))
print(decode_morse('.'))
 
# toto = 'a b  c d'
# toto = toto.replace('   ', '  ')
# print(toto.split(' '))
