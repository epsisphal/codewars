# Ones and Zeros

import codewars_test as test

# def binary_array_to_number(arr):
#     out = 0
#     for i in range(0, len(arr)):
#       if arr[i] == 1:
#             out = 2**(len(arr)-i-1) + out
#     return(out)

# def binary_array_to_number(arr):
#     out = 0
#     for i in range(0, len(arr)):
#         out += arr[i]*2**(len(arr)-i-1)
#     return(out)

def binary_array_to_number_alexis(arr):
    return(sum([arr[i]*2**(len(arr)-i-1) for i in range(0, len(arr))]))

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(binary_array_to_number([0,0,0,1]), 1)
        test.assert_equals(binary_array_to_number([0,0,1,0]), 2)
        test.assert_equals(binary_array_to_number([1,1,1,1]), 15)
        test.assert_equals(binary_array_to_number([0,1,1,0]), 6)

