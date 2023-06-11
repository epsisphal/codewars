# Integers: Recreation one from CodeWar
import codewars_test as test
import math

def list_squared_v1(m, n):
    #  This is too slow
    out = []
    for i in range(m, n+1):
        sum_squared_divisors = sum([j**2 for j in range(1, i+1) if (i/j).is_integer()])
        if math.sqrt(sum_squared_divisors).is_integer():
            out.append([i, sum_squared_divisors])
    return out

def list_squared(m, n):
    out = []
    for i in range(m, n+1):
        divisors = []
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                divisors.append(j**2)
                if j != i // j:
                    divisors.append((i // j)**2)
        sum_squared_divisors = sum(divisors)
        if math.sqrt(sum_squared_divisors).is_integer():
            out.append([i, sum_squared_divisors])
    return out

@test.describe('Tests...')
def _():
    @test.it('Fixed Tests')
    def _():
        test.assert_equals(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
        test.assert_equals(list_squared(42, 250), [[42, 2500], [246, 84100]])
        test.assert_equals(list_squared(250, 500), [[287, 84100]])


