# Return negative from Codewars
import codewars_test as test

def make_negative( number ):
    """
    Return the negative of `number` if it is positive, otherwise return `number`.
    """
    return -number if number > 0 else number


@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        for n, expected in ((42,-42), (-9,-9), (0,0)):
            actual = make_negative(n)
            message = f"For n = {n}, expected {expected} but got {actual}"
            test.assert_equals(actual, expected, message)


