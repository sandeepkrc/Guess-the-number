import random
print(" lets try your luck")
name=input("enter your name  ")
b=random.randint(0,5)
while True:   
    num=int(input("enter a number  "))
    
    if b==num:
        print("congs mr",name,"you win")
        break
    print("you lose...try again")
   

