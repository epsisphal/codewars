# Sentence Smash by Codewars

import codewars_test as test

def smash_v1(words):
    out = ""
    for i in words:
        out = out+' '+i
    return out[1:]

def smash(words):
    return  "".join(words[i]+" " for i in range(0, len(words)))[:-1]

def smash_solution(words):
    return " ".join(words)

@test.describe("smash")
def _():
    @test.it("Should return empty string for empty array.")
    def _():
        test.assert_equals(smash([]), "")
        
    @test.it("One word example should return the word.")
    def _():
        test.assert_equals(smash(["hello"]), "hello")
        
    @test.it("Multiple words should be separated by spaces.")
    def _():
        test.assert_equals(smash(["hello", "world"]), "hello world")
        test.assert_equals(smash(["hello", "amazing", "world"]), "hello amazing world")
        test.assert_equals(smash(["this", "is", "a", "really", "long", "sentence"]), "this is a really long sentence")

# print(smash(["hello", "amazing", "world"]))
