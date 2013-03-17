class TextChecker:
        checkString =  ""
        
        # param str: string or file
        def read(self,str):
                self.checkString = ""
                for line in str: self.checkString += line
                return len(self.checkString)

        # param str: string or file
        def check(self,str):
                buf = ""
                for line in str: buf += line
                buf = buf.split()
                result = {}
                for word in buf: result[word] = self.checkString.count(word)
                return result

        # search for words in source
        def tc(self,**option):
                output = {}
                output["len"] = self.read(option["source"])
                output["count"] = self.check(option["words"])
                return output

class TextCheckerTester:
        def input_by_string(self):
                text = TextChecker()
                input1 = "this is test words."
                input2 = "this is test apples"
                expect = {'count': {'this': 1, 'test': 1, 'is': 2, 'apples': 0}, 'len': 19}
                actual = text.tc(source=input1,words=input2)
                assert actual == expect
                return actual

test = TextCheckerTester()
test.input_by_string()
