# Digit*Digit from Codewars

import codewars_test as test

def square_digits(num):
    # Convert to string
    num = str(num)
    # Create empty string to store result
    result = ''
    # Loop through string
    for i in num:
        # Square each digit and add to result
        result += str(int(i)**2)
    # Return result as int
    return int(result)


@test.describe("Premade tests: ")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(square_digits(9119), 811181)
        test.assert_equals(square_digits(0), 0)

