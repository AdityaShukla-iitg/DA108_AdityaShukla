import random


def ask_choices():
    player_choice = input("Enter the choices from rock, paper , scissor : ")
    options=["rock" , "paper" , "scissor"]
    computer_choice= random.choice(options)

    choices={"Your_choice":player_choice , "Computer_choice":computer_choice}
    return choices



def check_winner(player , computer):
    print(f"You chose {player}, computer chose {computer}")

    if player == computer :
        return "It is a tie , looks like we need one more try"
    

    
    if player == "paper":
        if computer == "rock":
            return "You win the game , looks like you have a good day"
        if computer == "scissor":
            return "This time winner is one and only smart computer"
        

        
    if player =="rock":
        if computer == "paper":
         return "This time winner is one and only smart computer"
         
        if computer == "scissor":
            return "You win the game , looks like you have a good day"
        


    if player =="scissor":
        if computer == "scissor":
         return "This time winner is one and only smart computer"
         
        if computer == "paper":
            return "You win the game , looks like you have a good day"
        

obtained= ask_choices()
result = check_winner(obtained["Your_choice"], obtained["Computer_choice"])
print(result)

            