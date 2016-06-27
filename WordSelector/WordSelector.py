import random



class aWordSelector(object):

    def __init__(self):
        self.myList = self.openList("wordlist.txt")
        #random.seed(1234)
        self.myWord = self.myList[random.randint(1,len(self.myList)-1)]
        #print self.myWord

    def openList(self, filename):
        self.myList = open(filename)
        return self.myList.readlines()

    @property
    def myWord(self):
        return self._myWord.replace('\n', '').replace('\r', '')

    @myWord.setter
    def myWord(self, val):
        self._myWord = val

