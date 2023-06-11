# Sum of digits from CodeWars
import codewars_test as test

def digital_root_v1(n):
    out = 0 
    for i in range(0, len(str(n))):
        out += (n % 10)
        n = int(n/10)
    return out
    
def digital_root_v2(n):
    out = 0
    for i in str(n):
        out += int(i)
    return out

def digital_root(n):
    while len(str(n)) != 1:
        n = sum(int(i) for i in str(n))
    return n


@test.describe("Sum of Digits / Digital Root")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(digital_root(16), 7)
        test.assert_equals(digital_root(942), 6)
        test.assert_equals(digital_root(132189), 6)
        test.assert_equals(digital_root(493193), 2)

