from HM_manage import HMmanager

HMMan = HMmanager()
HMMan.printProperties()
try:
    var = HMMan.askForInput()
except IOError as ex:
    print ("can't be longer than 1!")
    HMMan.askForInput()