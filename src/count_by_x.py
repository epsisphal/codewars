# Count by X from Codewars
import codewars_test as test

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [i * x for i in range(1, n + 1)]

@test.describe("Fixed Tests")
def basic_tests():
    @test.it("Fixed tests")
    def fixed_tests():   
        test.assert_equals(count_by(1, 5), [1, 2, 3, 4, 5])
        test.assert_equals(count_by(2, 5), [2, 4, 6, 8, 10])
        test.assert_equals(count_by(3, 5), [3, 6, 9, 12, 15])
        test.assert_equals(count_by(50, 5), [50, 100, 150, 200, 250])
        test.assert_equals(count_by(100, 5), [100, 200, 300, 400, 500])

