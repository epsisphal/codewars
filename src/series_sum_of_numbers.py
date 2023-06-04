# Beginner Series #3 Sum of Numbers from Codewars

import codewars_test as test

def get_sum(a,b):
    if a > b:
        a,b = b,a
    return sum(range(a,b+1))

@test.describe('Sum of numbers')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(get_sum(0,1),1)
        test.assert_equals(get_sum(0,-1),-1)

