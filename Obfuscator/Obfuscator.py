
class aObfuscator(object):
    def __init__(self, word):
        self.obfuscatedWord = ""
        self.normalWord = word
        self.numberOfSpaces = len(self.getWordAsList(self.normalWord))
        self.obfuscateWord()

    def obfuscateWord(self):
        self.obfuscatedList = self.getWordAsList(self.normalWord)
        for i in range(0 ,len(self.normalWord )):
            self.obfuscatedList[i] ='_'
        self.obfuscatedWord= "".join(self.obfuscatedList)

    def getWordAsList(self, word):
        return list(word)

    def checkChar(self, char):
        self.found = False
        self.normalList = self.getWordAsList(self.normalWord)
        self.obfuscatedList=self.getWordAsList(self.obfuscatedWord)
        for i in range(0, len(self.normalList)):
            if(self.normalList[i]==char):
                if (self.obfuscatedList[i]==char):
                    return True
                self.obfuscatedList[i]=char
                self.numberOfSpaces -=1
                self.found = True

        self.obfuscatedWord= "".join(self.obfuscatedList)
        return self.found






