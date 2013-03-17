class TextChecker:
        source =  ""
        def read(self,str):
                self.source = ""
                for line in str: self.source += line
                return len(self.source)
     
        def check(self,str):
                buf = ""
                for line in str: buf += line
                words = buf.split()
                result = {}
                for word in words: result[word] = self.source.count(word)
                return result

        # search for words in source
        def tc(self,**option):
                output = {}
                output["len"] = self.read(option["source"])
                output["count"] = self.check(option["words"])
                return output

