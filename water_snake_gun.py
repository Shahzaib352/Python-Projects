# Snake, Water, Gun Game
 
'''
Snake = 1
Water = -1
Gun = 0

'''

import random  # Importing a 'random' <module>

print("Yeahhh! Let's Play Snake, Water, and Gun Game!")  # Print a Comment

while True:
    print(
    '''
    Please Enter : 
    => 's' for Snake 
    => 'w' for Water 
    => 'g' for Gun 
    '''
    )
    computer=random.choice([-1,0,1])   # Here Computer choses at rendom
    user_choice = input("Enter your choice : ")   # User will add his choice
    choice_dict = {"s": 1, "w":-1, "g":0}         # Will give user coice to computer
    reverse_dict = {1:"Snake", -1:"Water", 0:"Gun"}  # Will help to print the value of user choice

    user = choice_dict[user_choice] # 'user' will get the value when user will enter the 'key'

    print(f"You chose : {reverse_dict[user]}\nComputer chose : {reverse_dict[computer]}")  # Will print the both choices

    if(computer == user):      # Conditions
        print("Its a Draw!")
    else:
        if(computer == 1 and user == 0):
            print("You Win!")    
        elif(computer == 1 and user == -1):
            print("You Lose!")    
        elif(computer == 0 and user == 1):
            print("You Lose!")    
        elif(computer == 0 and user == -1):
            print("You Win!")    
        elif(computer == -1 and user == 0):
            print("You Lose!")    
        elif(computer == -1 and user == 1):
            print("You Win!")    

    if input("Do you want to play again? y/n").lower() != y:
        break
    
    
