# Is it a triangle from Codewars

import codewars_test as test

def is_triangle_alexis(a, b, c):
    return max([a, b, c]) < a+b+c-max(a, b, c)

def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(is_triangle(1, 2, 2), True, "didn't work when sides were 1, 2, 2")
        test.assert_equals(is_triangle(7, 2, 2), False, "didn't work when sides were 7, 2, 2")
        test.assert_equals(is_triangle(1, 2, 3), False, "didn't work when sides were 1, 2, 3")
        test.assert_equals(is_triangle(1, 3, 2), False, "didn't work when sides were 1, 3, 2")
        test.assert_equals(is_triangle(3, 1, 2), False, "didn't work when sides were 3, 1, 2")
        test.assert_equals(is_triangle(5, 1, 2), False, "didn't work when sides were 5, 1, 2")
        test.assert_equals(is_triangle(1, 2, 5), False, "didn't work when sides were 1, 2, 5")
        test.assert_equals(is_triangle(2, 5, 1), False, "didn't work when sides were 2, 5, 1")
        test.assert_equals(is_triangle(4, 2, 3), True, "didn't work when sides were 4, 2, 3")
        test.assert_equals(is_triangle(5, 1, 5), True, "didn't work when sides were 5, 1, 5")
        test.assert_equals(is_triangle(2, 2, 2), True, "didn't work when sides were 2, 2, 2")
        test.assert_equals(is_triangle(-1, 2, 3), False, "didn't work when sides were -1, 2, 3")
        test.assert_equals(is_triangle(1, -2, 3), False, "didn't work when sides were 1, -2, 3")
        test.assert_equals(is_triangle(1, 2, -3), False, "didn't work when sides were 1, 2, -3")
        test.assert_equals(is_triangle(0, 2, 3), False, "didn't work when sides were 0, 2, 3")

