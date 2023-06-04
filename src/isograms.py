# Isograms from Codewars

import codewars_test as test

# def is_isogram_v1(string):
#     if len(string) != len(set(string.lower())):
#         out = False
#     else:
#         out = True
#     # print(len(set(string.lower())))
#     return(out)

def is_isogram(string):
    return(False if len(string) != len(set(string.lower())) else True)

def is_isogram_solution(string):
    return len(string) == len(set(string.lower()))

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():      
        test.assert_equals(is_isogram("Dermatoglyphics"), True )
        test.assert_equals(is_isogram("isogram"), True )
        test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
        test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
        test.assert_equals(is_isogram("isIsogram"), False )
        test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )


