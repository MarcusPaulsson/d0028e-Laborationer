'''
Program för att beräkna sockerkaksrecept för godtyckligt många
personer 
@author: Marcus Paulsson
'''

# Funktion för receptet för X antal personer 
def recept(antal):
    print("Sockerkaka för",antal,"personer")
    print((antal*3)//4,"st ägg")
    print(antal*0.75,"dl socker")
    print(antal/2,"tsk vaniljsocker")
    print(antal/2,"tsk bakpulver")
    print(antal*0.75,"dl vetemjöl")
    print(antal*18.75,"gram smör")
    print(antal/4,"dl vatten\n")
    
# Funktion för att blanda ingredienserna för X antal personer
def tidblanda(antal):
    return 10+antal

# Funktion för att grädda kakan för X antal personer
def tidgradda(antal):
    return 30+antal*3

# Funktion för att redovisa totala informationen för sockerkakan
def sockerkaka(antal):
    recept(antal)
    print("Den totatla tiden för att blanda och grädda är"
          ,tidblanda(antal)+tidgradda(antal),"minuter")
    print("-"*20)
    
# Anrop som visar recept för 4 och 7 personer
def sockerkaka4_7():
	sockerkaka(4)
	sockerkaka(7)



