from Obfuscator import Obfuscator
from WordSelector import WordSelector




class HMmanager(object):
    def __init__(self):
        self.myLives = 5
        self.winState = 0 #0 = ongoing, 1 won, -1 lost
        self.mySelector = WordSelector.aWordSelector()
        self.myWord = self.mySelector.myWord
        self.myObfuscator = Obfuscator.aObfuscator(self.myWord)

    def printProperties(self):
        print "normal word is %s" % self.myObfuscator.normalWord
        print "obf word is %s" % self.myObfuscator.obfuscatedWord

    def checkCharacter(self, myChar):
        if self.myObfuscator.checkChar(myChar):
            print self.myObfuscator.obfuscatedWord
        else:
            print (myChar + " is not in this word!")
            self.myLives -= 1
        self.checkWinOfLoss()


    def checkWinOfLoss(self):
        if self.myObfuscator.numberOfSpaces == 0:
            self.winGame()
            return
        if self.myLives <= 0:
            self.loseGame()
            return


    def askForInput(self):
        print "you have these lives: " + self.printLives()
        prompt = '>'
        ask = raw_input(prompt)
        if (ask.__len__() > 1):
            raise IOError
        if (ask.__len__() == 1):
            self.checkCharacter(ask)
        try:
            self.askForInput()
        except IOError:
            print ("can't be longer than 1!")


    def printLives(self):
        toPrint = ""
        for i in range(0, self.myLives):
            toPrint += "*"
        return toPrint


    def winGame(self):
        self.winState = 1
        print("you win!")


    def loseGame(self):
        self.winState = -1
        print("you lose")
        print("the word was " + self.myObfuscator.normalWord)
