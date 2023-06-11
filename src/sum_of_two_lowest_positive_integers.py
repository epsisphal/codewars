# Sum of two lowest positive integers in Codewars

import codewars_test as test

def sum_two_smallest_numbers_alexis(numbers):
    min_1 = min(numbers)
    numbers.pop(numbers.index(min(numbers)))
    min_2 = min(numbers)
    return(min_1+min_2)

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
        test.assert_equals(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
        test.assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)


