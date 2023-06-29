#create a main method to run a game of rock paper scissors
def main():
    #create a variable to store the user's choice
    user_choice = input("Enter rock, paper, or scissors: ")
    #create a variable to store the computer's choice
    computer_choice = "rock"
    #print out the user's choice
    print("You chose: " + user_choice)
    #print out the computer's choice
    print("The computer chose: " + computer_choice)
    #create an if statement to determine who won
    if user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
    elif user_choice == "rock" and computer_choice == "paper":
        print("You lost!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("You lost!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won!")
    elif user_choice == "scissors" and computer_choice == "rock":
        print("You lost!")
    else:
        print("It's a tie!")
        


        