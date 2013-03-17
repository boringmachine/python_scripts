class TextChecker:
        checkString =  ""
        def read(self,str):
                self.checkString = ""
                for line in str: self.checkString += line
                return len(self.checkString)
     
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

