# Most frequently used word from CodeWars
# --> Reading comments on the site, it seems that the random tests are not correct. 

import codewars_test as test
import string
import numpy as np

def check_word(word):
    return any(char.isalpha() for char in word)

def top_3_words(text):
    text = ''.join([char for char in text.lower() if char not in string.punctuation or char == "'"])
    words = [i for i in text.split() if check_word(i) is True]
    unique_words = list(set(words))
    words_count = []
    for i in range(0, len(unique_words)):
        words_count.append(words.count(unique_words[i]))
    indices = np.argpartition(words_count, -min(3, len(unique_words)))[-min(3, len(unique_words)):]
    my_array = np.array(words_count)
    indices = indices[np.argsort(-my_array[indices])]
    return [unique_words[indices[i]] for i in range(0, min(3, len(indices)))]

def top_3_words_not_working(text):
    return [i[0] for i in sorted({i.lower(): text.lower().split().count(i) for i in text.lower().split() if i.isalpha()}.items(), key=lambda x: x[1], reverse=True)[:3]]

@test.describe("Top 3 words")
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
        test.assert_equals(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
        test.assert_equals(top_3_words("  //wont won't won't "), ["won't", "wont"])
        test.assert_equals(top_3_words("  , e   .. "), ["e"])
        test.assert_equals(top_3_words("  ...  "), [])
        test.assert_equals(top_3_words("  '  "), [])
        test.assert_equals(top_3_words("  '''  "), [])
        test.assert_equals(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])

# text = """In a village of La Mancha, the name of which I have no desire to call to
# #         mind, there lived not long since one of those gentlemen that keep a lance
# #         in the lance-rack, an old buckler, a lean hack, and a greyhound for
# #         coursing. An olla of rather more beef than mutton, a salad on most
# #         nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# #         on Sundays, made away with three-quarters of his income."""

# text = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

# text = "  //wont won't won't "
# print(top_3_words(text))

