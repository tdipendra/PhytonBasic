
# name="Dipendra Thapa"
#classs = "BTECH"

#print(name)
#print(classs)
#print(name,classs)
#print(name,classs,123,"test word ")
#element=0
#print(element)

#num = int(input ("enter the any number"))

#if num == 0 :
    #print("it is an zero",num)
#elif num < 1:
  #  print("it is an negative nunber",num)
#else:
 #   print("it is an posiitbe number",num)
    
#prime numbers solution

""

import  turtle
import random


def add(x1,x2):
    answer=x1+x2;
    print(" your answer is : " + str(answer))
    
def sub(x1,x2):
    answer=x1-x2;
    print(" your answer is : " + str(answer))
    
    
def multi(x1,x2):
    answer=x1*x2;
    print(" your answer is : " + str(answer))
    
    
def div(x1,x2):
    if x2==0:
        print(" this division cannot be done because x2 cannot be zero ")
        return
    answer=x1/x2;
    print(" your answer is : " + str(answer))
    
    
def circle(n):
    
    turtle.speed(0)
    
    while (n !=0):
        size = random.randint(30,100)
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        
        turtle.circle(size)
        n-=1
        
    turtle.done()
    
    
    

def menu():
    
    choice=-124981221412
    while (choice!=6):
        print" ------------- "
        print" this is a calculator "
        print" ------------- "
        print(" 1.ADD ")
        print(" 2.SUB ")
        print(" 3.MUL ")
        print(" 4.DIV ")
        print(" 5.TUR ")
        print(" 6.Q ")
        
        
        choice = int(input(" what is your choice:? "))
        
        
        if choice == 1:
            x1=float(input(" enter the first number to add? "))
            x2=float(input(" enter the second number to add with x1? "))
            add(x1,x2)
            
        elif choice ==2:
            x1=float(input(" enter the first number to subtract ? "))
            x2=float(input(" enter the second number to sbutract from x1 ? "))
            sub(x1,x2)
            
        elif choice ==3:
            x1=float(input(" enter the first number to multiple ? "))
            x2=float(input(" enter the second number to multiple with x1 ? "))
            multi(x1,x2)
            
        elif choice ==4:
            x1=float(input(" enter the first number to divide ? "))
            x2=float(input(" enter the second number to dive x1 ? "))
            div(x1,x2)
            
        elif choice ==5:
            n= float(input(" how many to circle you want to draw? "))
            circle(n)
            
        elif choice ==6:
            break
            
        else:
            print(" the entered command is invalid ")
    
    
    

def main():
    
    menu()
    
    
main() 




""

    
    
    
                    
        