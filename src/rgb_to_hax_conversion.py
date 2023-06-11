# RGB to Hex Conversion from CodeWars
import codewars_test as test

def rgb_v1(r, g, b):
    # This is unfinished. 
    return ''.join(('0'+str(hex(i))[2:].upper())[-2:] for i in {b, g, r})

def rgb(r, g, b):
    out = ''
    for i in (r, g, b):
        # i = max(0, i)
        # i = min(255, i)
        i = min(255, max(i, 0))
        out = out+('0'+str(hex(i))[2:].upper())[-2:]
    return out

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Tests")
    def _():
        test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
        test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
        test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
        test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
        test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")


