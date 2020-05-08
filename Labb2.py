'''
Program för olika iterativa och rekursiva metoder
@author: Marcus Paulsson
'''

# Uppgift1--------------------------------------------------
def logStar(x):
    import math
    count=0
    while x>1:
        x=math.log(x,2)
        count+=1
    return count

# Uppgift2--------------------------------------------------
def tvarsumman(n):
  if n==0:
    return 0
  else:
    return n%10+tvarsumman(n//10)
#alt: return n%10+tvarsumman((n-n%10)/10)

# Uppgift3--------------------------------------------------
def avbetalningsplan(skuld, räntesats, belopp):
    print("\nÅrlig avbetalning:",belopp)
    print("Räntesats:",räntesats*100, "%")
    print("Ingående skuld:",skuld)
    yearCount=0
    
    while skuld>0:
        yearCount=yearCount+1
        temp_ränta=räntesats*skuld
        amorterat=belopp-temp_ränta
        skuld-=amorterat
        if(skuld<0):
            amorterat=skuld+belopp-temp_ränta
            skuld-=skuld
        print("\n-- År",yearCount,"--")
        print("Återstående skuld: ",skuld)
        print("Amorterat belopp:  ",amorterat)  
        print("Ränta:             ",temp_ränta)
               
# Uppgift4 (5a, 5b) ----------------------------------------
def derivate(f,x,h):
    return (1/(2*h))*((f(x+h))-(f(x-h)))

def solve(f,x0,h):
    x_temp=x0
    x_approx = x_temp-(f(x_temp)/derivate(f,x_temp,h))
    while (abs(x_temp-x_approx) >= h):
        x_temp=x_approx
        x_approx = x_temp-(f(x_temp)/derivate(f,x_temp,h))
        
    return x_approx

# Exempelfunktioner för test av "solve"-funktionen
def f_test1(x):
    return  x**2-1
def f_test2(x):
    return 2**x-1
def f_test3(x):
    return x**2+2*x+1
def f_test4(x):
    return x-math.e**(-x)          

# Import av testfiler för att kolla funktionerna------------
import d0028e_lab2_logStarTest
import d0028e_lab2_sumTest
import d0028e_lab2_solveTest

avbetalningsplan(100, 0.05, 25)
