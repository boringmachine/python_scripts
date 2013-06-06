from UglyCipher import *

class UglyCipherTester:
        def input_by_string(self):
                uc   = UglyCipher()
                word = "this is test words."
                key    = 5
                c      = 'x'
                a      = 4
                actual = uc.buildCipher(word,key,c,a)
                # assert actual == expect
                return actual

test = UglyCipherTester()
print test.input_by_string()
