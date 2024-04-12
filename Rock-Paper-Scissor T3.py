import random

print ("Welcome to 'Rock-Paper-Scissors' Game by Harshit Nashine")
print("\nRules:\nRock vs Paper - Paper Wins \nPaper vs Scissors - Scissors wins\nScissors vs Rock - Rock Wins")

choices = ["Rock", "Paper", "Scissors"]

while True:
    User_choice=(int(input("\nChoose Your Move:\n 0 for Rock\n 1 for Paper\n 2 for Scissors\nEnter Your Choice- ")))

    if User_choice >= 3 or User_choice < 0:
       print("Invalid Choice")
    else:
       computer_choice = random.randint(0,2)
       print("\nComputer Chose:",choices[computer_choice])
       print("You Chose:",choices[User_choice])
       
       if computer_choice == User_choice:
           print("\nIt's a 'Tie'")
       elif computer_choice == 0 and User_choice == 2:
           print("\nYou 'Lose'")
       elif User_choice == 0 and computer_choice == 2:
           print("\nYou 'Win'")
       elif computer_choice > User_choice:
           print("\nYou 'Lose'")
       elif User_choice > computer_choice:
           print("\nYou 'Win'")
    
    play_again = input("\nDo you want to play again? Press [Y] for yes/ no: ").lower()
    if play_again != 'y':
        break