# Two to one from Codewars

import codewars_test as test
    
def longest_alexis(a1, a2):
    concat = sorted(a1+a2)
    out = []
    out.append(concat[0])
    for i in range(1, len(concat)):
            if concat[i] != concat[i-1]:
                  out.append(concat[i])
    return(''.join(out))

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

@test.describe("longest")
def tests():
    @test.it("basic tests")
    def basics():
        test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
        
        