# Split Strings from Codewars
import codewars_test as test

def solution_v1(s):
    if len(s) % 2 == 1:
        s = s+'_' 
    out = []
    j = 0
    for i in range(0, int(len(s)/2)):
        out.append(s[j]+s[j+1])
        j = j+2
    return(out) 

def solution_v2(s):
    s = s+'_' 
    out = []
    j = 0
    for i in range(0, int(len(s)/2)):
        out.append(s[j]+s[j+1])
        j = j+2
    return(out) 

def solution_v3(s):
    s = s+'_'
    out = []
    out.extend(s[2*i] + s[2*i+1] for i in range(0, int(len(s)/2)))
    return out

def solution(s):
    s= s+'_'
    return [s[2*i] + s[2*i+1] for i in range(0, int(len(s)/2))]

test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)




