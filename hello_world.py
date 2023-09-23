import random
items = ["rock","paper","scissor"]

won= None
while won is None:   
    option = input("Enter the items :") 
    if option not in items:
        print("Please type valid input")
        continue  

    computer = (random.choice(items))
    print(f" computer input is {computer}")
    if option=="rock" and computer== "scissor":
        print("you won")
        break
    elif option=="scissor" and computer== "paper":
        print("you won")
        break
    elif option=="paper" and computer== "rock":
        print("you won")
        break
   
    elif option==computer:
        print("tie")
        continue
    else:
        print('you Failed, Try again')
        continue

    

        
        

        
    
        

        
        
            



    
