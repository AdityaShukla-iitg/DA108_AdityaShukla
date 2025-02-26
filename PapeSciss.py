# Subject: Rock-Paper-Scissors Game
# This game demonstrates the use of:
# 1. Lists: To store possible choices for the user and computer.
# 2. Dictionaries: For mapping the winning conditions.
# 3. Random Module: To randomly assign a choice to the computer.
# 4. Input Validation: Ensures the user enters valid choices.
# 5. Control Structures:
#    - Nested `if` statements (used previously, now refactored). Line number 31-50
#    - `elif` for decision-making. Line number 61-88
#    - Dictionary-based win logic (current implementation).Line number 97-101



import random



def get_choice():
    option_user = ["rock" , "paper" , "scissor"]                                                           #creating options for user
    while True:
        player_choice = input("Enter choices from rock, paper , scissor : ").lower()                       #taking valid input from user
        if player_choice in option_user:
            break

        print("Your choice is invalid please choose from rock , paper , scissor")
    
    option_computer=["rock","paper" , "scissor"]                                                           #Creating a list of choices for comp

    computer_choice = random.choice(option_computer)                                                       #Alloting choices randmoly from list

    choices = {"You_chose":player_choice,"computer_chose":computer_choice}                                 #dictionary which shows who chose what!

    return choices

def check_win(player , computer):                                                                          #def win function with 2 variable container
    print(f"You chose {player} , computer chose {computer}")                                               #printing the all options by user and comp
    
    if player == computer:
        return "It is a tie , looks like we need one more try" 
    
    win_cond={"rock": "scissor" ,"paper":"rock", "scissor":"paper"}                                     #Using dictionary logic
    if win_cond[player]==computer:
        return "You win the game , looks like you have a good day"
    else :
        return "This time winner is one and only smart computer"
    
    
    
    
    
    
    
                                                #Using elif & if to predict winner
    
    # elif player=="rock" and computer =="paper":
    #     return "This time winner is one and only smart computer"
    
    # elif player=="rock" and computer=="scissor":
    #     return "You win the game , looks like you have a good day"
    
    # elif player=="paper" and computer == "scissor":
    #     return "This time winner is one and only smart computer"
    
    # elif player=="paper" and computer=="rock":
    #     return "You win the game , looks like you have a good day"
    
    # elif player=="scissor" and computer =="rock":
    #     return "This time winner is one and only smart computer"
    
    # elif player == "scissor" and computer=="paper":
    #     return "You win the game , looks like you have a good day"
    







    

    # if player == computer :
    #     return "It is a tie , looks like we need one more try"                                           #try with nested if to predict winner
    

    
    # if player == "paper":
    #     if computer == "rock":
    #         return "You win the game , looks like you have a good day"
    #     if computer == "scissor":
    #         return "This time winner is one and only smart computer"
        

        
    # if player =="rock":
    #     if computer == "paper":
    #      return "This time winner is one and only smart computer"
         
    #     if computer == "scissor":
    #         return "You win the game , looks like you have a good day"
        


    # if player =="scissor":
    #     if computer == "scissor":
    #      return "This time winner is one and only smart computer"
         
    #     if computer == "paper":
    #         return "You win the game , looks like you have a good day"








   
        

    
response = get_choice()                                                                                   #Storing the value of choices in response
result = check_win(response["You_chose"], response["computer_chose"])                                     #pass the arg in check fn wpecifically in containers

print(result)  