# -*- coding: latin-1 -*-

import sys
import __main__

def testSum(fkn, printName, num, correctOutput):

  print("Testar "+printName+"("+str(num)+")...")

  sum = fkn(num)

  if sum==correctOutput:
    print("funkar!")
  else:
    print("funkar inte!")
    print("   Testresultat:  ",sum)
    print("   Rätt resultat: ",correctOutput)

testSum(__main__.tvarsumman, "tvarsumman", 123, 6)
testSum(__main__.tvarsumman, "tvarsumman", 0, 0)
testSum(__main__.tvarsumman, "tvarsumman", 7619, 23)
