# -*- coding: latin-1 -*-

import sys
import __main__

def testLogStar(fkn, printName, num, correctOutput):

  print("Testar "+printName+"("+str(num)+")...")

  output = fkn(num)

  if output==correctOutput:
    print("funkar!")
  else:
    print("funkar inte!")
    print("   Testresultat:  ",output)
    print("   Rätt resultat: ",correctOutput)

testLogStar(__main__.logStar, "logStar", 1,0)
testLogStar(__main__.logStar, "logStar", 2,1)
testLogStar(__main__.logStar, "logStar", 3,2)
testLogStar(__main__.logStar, "logStar", 4,2)
testLogStar(__main__.logStar, "logStar", 12345,4)
