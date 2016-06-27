import unittest
from Obfuscator import Obfuscator
from WordSelector import WordSelector
import HM_manage

class unitTest(unittest.TestCase):


    def testOngoing(self):
        myManager = HM_manage.HMmanager()
        myManager.myObfuscator = Obfuscator.aObfuscator("testWord")
        myManager.checkCharacter('a')
        self.assertEqual(myManager.winState, 0)

    def testRun(self):
        myManager = HM_manage.HMmanager()
        myLives = myManager.myLives
        myManager.myObfuscator = Obfuscator.aObfuscator("testWord")
        myManager.checkCharacter('a')
        self.assertEqual(myManager.myLives,myLives-1)

    def testLoss(self):
        myManager = HM_manage.HMmanager()
        myLives = myManager.myLives
        myManager.myObfuscator = Obfuscator.aObfuscator("testWord")
        for i in range(0, myLives):
            print myManager.myLives
            myManager.checkCharacter('a')
        self.assertLess(myManager.winState, 0)


