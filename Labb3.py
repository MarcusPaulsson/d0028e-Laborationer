'''
Program för olika lagringsmetoder
@author: Marcus Paulsson
'''

####### FUNKTIONER ALLA LÖSNINGAR ANVÄNDER #######   
    
#Funktion som skriver ut när man anger felaktigt tecken för menyn.    
def errorInput(): 
    print("\nInsert a number from the list!\n--------------")
    
#Funktion som behandlar menyvalet.
def menu_choice(storageType): 
    print("Menu for", storageType,"\n 1: Insert \n 2: Lookup \n 3: Exit program\n")
    i=input("Choose alternative: ")
    return i

#---------------------------------------------

######## LÖSNING 1: LISTOR ########
    
def main_list():
    
    list_word=[] #lista för orden skapas 
    list_description=[] #lista för beskrivningen skapas
    while True:
        i=menu_choice("list") # Värdet på i fås av funktionen som körs
        
        if i=='1':    # Alternativet för att lägga in ord med beskrivning.
            listorAlt1(list_word, list_description)
            
        elif i=='2':  # Alternativet för att söka upp beskrivning av ord.
            listorAlt2(list_word, list_description)
            
        elif i=='3':  # Avslutar programmet
            break
        else:
            errorInput()

##### Funktioner som används i lösning 1: listor #####
            
def listorAlt1(list_word, list_description): #Funktion för att sätta in ord i ordlistan (listor).
    word=input("Word to insert: ")
    
    if word in list_word: # Kollar om den skrivna ordet redan finns i listan
        print(word+" allready exist in the list!\n")

    else: # Om ordet inte finns i listan läggs det in och så även beskrivningen
        list_word.append(word)
        temp_descript=input("Insert description: ")
        list_description.append(temp_descript)
        print("----------")
        
def listorAlt2(list_word, list_description): #Funktion för att söka upp ett ords beskrivning (listor).
    word=input("Word to lookup: ")
    if word in list_word: # Kollar om det skrivna ordet finns i listan, om det finns skrevs beskrivningen ut
        print("Description for",word,":",list_description[list_word.index(word)],"\n--------------") #skriver ut beskrivningen som finns på samma position som ordet man angav.                          
    else: 
        print("\n Word does not exist in list!\n")
    
#-----------------------------------------------

######## LÖSNING 2: TUPPLAR ########

def main_tuple():
 
    tupleList=[]#En lista för att lagra tupplar i skapas
    
    while True:
        i=menu_choice("tuple")# Värdet på i fås av funktionen som körs
            
        if i=='1':   # Alternativet för att lägga in ord med beskrivning.
            tuplerAlt1(tupleList)
            
        elif i=='2': # Alternativet för att söka upp beskrivning av ord.
            tuplerAlt2(tupleList)
           
        elif i=='3': # Avslutar programmet
            break
        else:
            errorInput()
            
##### Funktioner som används i lösning 2: tupplar #####

def tuplerAlt1(tupleList): #Funktion för att sätta in ord i ordlistan (tupler).
    word=input("Word to insert: ")
    inList=False
    
    for tupleWord, tupleDescrip in tupleList: # Kollar om den skrivna ordet redan finns i listan
        if tupleWord==word:
            print (word+" allready exist in the list! \n")
            inList=True # Boolean ändras till att den finns i listan
            return
            
    if inList==False:
        description=input("Description of: ")
        tupleList.append((word, description)) # ordet och beskrivningen sätts in som en tuple i "tupleList"
    
def tuplerAlt2(tupleList): #Funktion för att söka upp ett ords beskrivning (tupler).
    word=input("Word to lookup: ")
    found=False

    for tupleWord,tupleDescrip in tupleList: #En loop som letar bland alla värden i "tupleList"
            if tupleWord==word: # Om det angivna ordet finns i "tupleList" skrivs beskrivningen ut.
                print("\nDescription of ", word,": "+tupleDescrip+"\n----------------")
                found=True
                return
                
    if found==False:
        print("\n Word does not exist in the list!\n---------------")
#---------------------------------------------

######## LÖSNING 3: DICTIONARY ########

def main_dic(): 
    dic={} 
    while True:
        
        i=menu_choice("dictonary")# Värdet på i fås av funktionen som körs

        if i=='1':    # Alternativet för att lägga in ord med beskrivning.
            dictionaryAlt1(dic)
            
        elif i=='2':  # Alternativet för att söka upp beskrivning av ord.
            dictionaryAlt2(dic)
            
        elif i=='3':  # Avslutar programmet
            break
        else:
            errorInput()
            
#---- Funktioner som används i lösning 3: dictionary ----

#Funktion för att sätta in ord i ordlistan (dictionary).
def dictionaryAlt1(dic): 
    word=input("Word to insert: ")
    if word in dic.keys(): # Kollar om den skrivna ordet redan finns i "dic"
        print(word+" allready exist in the list! \n")
    else: # Om ordet inte finns...
        descrip=input("Description of word: ")
        dic[word]=descrip # ordet sätts som nykel till beskrivningen i "dic"


#Funktion för att söka upp ett ords beskrivning (dictionary).
def dictionaryAlt2(dic): 
    word=input("Word to lookup: ")
    if word in dic.keys(): # Kollar om den skrivna ordet finns i "dic"...
        print("\nDescription for", word,": "+dic[word]+"\n--------------") # Om det finns skrivs det ut via det ord (nykel) som angivits
    else: #Om det inte finns ges ett felmeddelande
        print("\nOrdet finns ej med i Ordlistan\n-------------")
#-----------------------------------------------
