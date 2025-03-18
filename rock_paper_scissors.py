# Rock, Paper, Scissors Game
 
'''
Rock = 1
Paper = -1
Scissors = 0

'''

import random  # Importing a 'random' <module>
if __name__ == "__main__":
    while True:
        print("Yeahhh! Let's Play Rock, Paper, and Scissors Game!")  # Print a Comment
        print(
        '''
        Please Enter : 
        => 'r' for Rock 
        => 'p' for Paper 
        => 's' for Scissors 
        '''
        )
        computer=random.choice([-1,0,1])   # Here Computer choses at rendom
        user_choice = input("Enter your choice : ")   # User will add his choice
        choice_dict = {"r": 1, "p":-1, "s":0}         # Will give user coice to computer
        reverse_dict = {1:"Rock", -1:"Paper", 0:"Scissors"}  # Will help to print the value of user choice

        user = choice_dict[user_choice] # 'user' will get the value when user will enter the 'key'

        print(f"You chose : {reverse_dict[user]}\nComputer chose : {reverse_dict[computer]}")  # Will print the both choices

        if(computer == user):      # Conditions
            print("Its a Draw!")
        else:
            if(computer == 1 and user == 0):
                print("You Lose!")    
            elif(computer == 1 and user == -1):
                print("You Win!")    
            elif(computer == 0 and user == 1):
                print("You Win!")    
            elif(computer == 0 and user == -1):
                print("You Lose!")    
            elif(computer == -1 and user == 0):
                print("You Win!")    
            elif(computer == -1 and user == 1):
                print("You Lose!")    
        if input("Do you want to play again? (y/n): ").lower() != "y":
            break
    
  
