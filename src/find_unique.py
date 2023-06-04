# Find unique number from CodeWars

import codewars_test as test

def find_uniq(arr):
    return max(arr) if arr.count(max(arr)) < arr.count(min(arr)) else min(arr)

@test.describe("Basic Tests")
def f():
    @test.it("Simple tests")
    def _():
        test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
        test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
        test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)


