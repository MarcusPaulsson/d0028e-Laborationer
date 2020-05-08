
#---------------------------------------------------------

#Deklarerar klassen
class Contact:
    def __init__(self, name, number): # Metoden som delar in indatan 
        self.name = name
        self.number=[]
       
        
#---------------------------------------------------------
        
# Funktion som kör programmet och tillkallar alla andra metoder
def lab4main():
    storageList=[] # skapar listan där all indata ska lagras
    phonebookMenu() # skriver ut menyalternativen
    while True:
        insert=input("> ") 
        try: 
            temp_choicelList=[] 
            temp_choiceList=insert.split() # Delar upp inslagna ord på olika platser i listan

            # Kollar om första ordet stämmer överens med alternativen
            if temp_choiceList[0] == 'create':
                create(temp_choiceList, storageList)
            
            elif temp_choiceList[0] == 'add':
                add(temp_choiceList, storageList)

            elif temp_choiceList[0] == 'lookup':
                lookup(temp_choiceList, storageList)

            elif temp_choiceList[0] == 'alias':
                alias(temp_choiceList, storageList)

            elif temp_choiceList[0] == 'delete':
                delete(temp_choiceList, storageList)

            elif temp_choiceList[0] == 'save':
                save(temp_choiceList, storageList)
                
            elif temp_choiceList[0] == 'load':
                load(temp_choiceList, storageList)

            elif temp_choiceList[0] == 'quit':
                avsluta()
                break
            elif temp_choiceList[0] == 'list':
                lista(storageList)
            else:
                print("Insert a command!") # Felmeddelande för ord som ej finns
        except  IndexError:
            print("Insert a command!")# Felmeddelande när inget skrivs in i listan


            #------------------------------------#
            # FUNKTIONER SOM ANROPAS I PROGRAMMET#
            #------------------------------------#

#----------------------------------------------------------------
            
#Funktion som skriver ut menyn
def phonebookMenu():
    print("-"*25)
    print("create (name)")
    print("Add (name + number)")
    print("Lookup (name)")
    print("delete (name + newname)")
    print("delete (name)")
    print("Save (filename)")
    print("Load (filename)")
    print("Quit")
    print("-"*25)
#-----------------------------------------------------------------

# Funktion för att skapa en kontakt.
def create(temp_choiceList,storageList):
    if len(temp_choiceList) == 2: # Kollar input-syntaxen
        
        for i in range(len(storageList)): # Loopar igenom hela lagringslistan och kollar om namnet eller numret redan finns
            if temp_choiceList[1] == storageList[i].name:
                print ("Error!, the name has already been stored!")
                return
    
    else:
        print("Error!, insert with the correct syntax (*create name*)")
        return
    storageList.append(Contact(temp_choiceList[1], [])) #Lagrar kontakten i lagringslistan och skapar en tom lista för att lagra telefonnummer.
#-----------------------------------------------------------------
    
#Funktion för att lägga till ett nummer till en kontakt
def add(temp_choiceList, storageList):
    if len(temp_choiceList) == 3:
        for i in range(len(storageList)): #loop för att kolla så kontakten finns skapad.
            if temp_choiceList[1] == storageList[i].name:
                for j in range(len(storageList[i].number)): # loop för att kolla så numret inte redan finns lagrat.
                    if storageList[i].number[j] == temp_choiceList[2]:
                        print("Error!, number already exists.")
                        return
            
        for i in range(len(storageList)): # när vi kollat att inget fel finns loopar vi igenom igen för att lägga in på rätt position
            if temp_choiceList[1] == storageList[i].name:
                storageList[i].number.append(temp_choiceList[2])
                return
        print("Error!, the name does not exists")
    else:
        print("Error!, insert with the correct syntax (*add name number*)")

#-----------------------------------------------------------------
    
#Funktion som söker efter numret för ett namn
def lookup(temp_choiceList, storageList):
    if len(temp_choiceList) == 2: # Kollar input-syntaxen
        for i in range(len(storageList)): # Loopar igenom hela lagringslistan och kollar om den finns som namn eller alias
            if temp_choiceList[1] in storageList[i].name:
                print("Numbers for "+temp_choiceList[1]+":")
                if len(storageList[i].number)==0:
                    print("No numbers stored")
                    return
                
                for j in range(len(storageList[i].number)):
                    print(storageList[i].number[j])
                return
        print("Error!, the name does not exist")
        return
    else:
        print("Error!, insert with the correct syntax (*lookup name*)")

#-----------------------------------------------------------------
        
        
#Funktion för att byta nummer för en kontakt
def delete(temp_choiceList, storageList):
    if len(temp_choiceList) == 3: # Kollar input-syntaxen för (*delete name + number*)

        for i in range(len(storageList)):
            if temp_choiceList[1] in storageList[i].name:
                for j in range(len( storageList[i].number)):
                    if temp_choiceList[2] == storageList[i].number[j]:  
                        del(storageList[i].number[j])
                        return
                print("number does not exists for this contact, cannot be deleted")
                return
        print("Name does not exists")
        return
    elif len(temp_choiceList) == 2:
        for i in range(len(storageList)):
            if temp_choiceList[1] == storageList[i].name:
                del(storageList[i])
                return
        print("Name does not exists.")
    else:
        print("Error!, insert with the correct syntax (*delete name number*) or (*delete name*)")

#-------------------------------------------------------------------
        
#Funktion som sparar en textfil med alla inlagda kontakter
def save(temp_choiceList,storageList):
    if len(temp_choiceList) == 2: # Kollar input-syntaxen
        with open(temp_choiceList[1]+".txt", "w") as file: #skapar och öppnar en skrivbar fil med det angivna namnet
            for i in range(len(storageList)):
                file.write(storageList[i].name +";")
                for j in range(len(storageList[i].number)):
                        file.write(storageList[i].number[j]+";")
                file.write("\n")
            file.close()
            return
    else:
        print("Error!, insert with the correct syntax (*save filename*)")

#-------------------------------------------------------------------
        
#Funktion som laddar in kontakter från en textfil
def load(temp_choiceList, storageList):
    if len(temp_choiceList) == 2: # Kollar input-syntaxen
        try:
            with open(temp_choiceList[1]+".txt", "r") as file: # Öppnar den angivna filen och läser in innehållet
                allLines = file.readlines()# Läser filen rad för rad
                storageList.clear() #Kastar bort det som evetuellt redan finns
                for i in range(len(allLines)):
                    loadList = allLines[i].split(";") # Delar upp datan på varje rad i en lista
                    storageList.append(Contact(loadList[0],[]))
                    temp_numList= loadList[1:-1]
                    for j in range(len(temp_numList)):
                        storageList[i].number.append(temp_numList[j])
    
        except FileNotFoundError:
             print("Error!, file does not exist")
        
    else:
        print("Error!, insert with the correct syntax (*load filename*)")
      
#---------------------------------------------------------------------

#Funktion för avslut för programmet
def avsluta():
    print("Exited!")

#kallar för att starta programmet direkt
lab4main()        






