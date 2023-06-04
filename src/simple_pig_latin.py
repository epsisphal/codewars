# Simple pig latin from Codewars
import codewars_test as test

def pig_it_alexis(text):
    out = ""
    for word in text.split():
        for i in range(1, len(word)):
            out = out+word[i]
        out = out+word[0]+'ay '
    return(out[:-1] if len(text.split()[-1]) != 1 else out[:-3])

def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

@test.describe("Basic Tests")
def f():
    @test.it("Simple tests")
    def _():
        test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
        test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')

# print(pig_it('Pig latin is cool'))

