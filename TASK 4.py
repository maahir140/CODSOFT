#              TASK:- 04
#              ROCK-PAPER-SCISSORS

import random

#Important game instruction 
print("Enter the choice")
print("1 for Game Instruction")
print("2 for Play Game")
print("3 for Quite the Game")

user1st = int(input("ENter Your choice: "))    # User chose what he/she do

if user1st == 1:         # Game Instruction
    print("Chosse your Option\n Once both the user and the computer have made their choices, the winner is determined based on the following rules:\n i.   Rock crushes scissors (Rock wins against scissors).\n ii.  Scissors cuts paper (Scissors win against paper).\n iii. Paper covers rock (Paper wins against rock).\n Winning rule:-\n 1. If your choice beats the computer's choice according to the rules mentioned above, you win the round.\n2. If the computer's choice beats yours, you lose the round.\n3, If both user and the computer choose the same weapon, the round is a tie.")

elif user1st == 2:       # Play Game
# Gives the option to user for choicess
   print("Enter the no. for choicing your option")
   print("1 for rock")
   print("2 for paper")
   print("3 for scissors")

# A function that Prompt the user to chosse rock, paper, scissors and print their choicess
   def userChoice():
      choice = int(input("Plz Enter you choice:- ")) # prompt input
      if choice == 1:
         return("rock")
      elif choice == 2:
         return("paper")
      elif choice == 3:
         return("scissor")
      else:
         return("Your choice not found !")

# A function that generate a random choice for computer
   def computerChoice():
      li = ['rock', 'paper', 'scissor']
      return random.choice(li)

# A function that determine the winner
   def winner(choice, com):
      if choice == com:
         return("Game tie!")
      elif (choice == 'rock' and com == 'scissor') or \
           (choice == 'paper' and com == 'rock') or \
           (choice == 'scissor' and com == 'paper'):
           return("You win!")
      else:
          return("Computer Wins!")

# # A function that displayed the result   
   def playGame():
      print("Let's play Rock, Paper, Scissors!")
      choice = userChoice()
      com = computerChoice()
      print("You chose:", choice)
      print("Computer chose: ", com)
      print(winner(choice, com))

   playGame() # Game play

   playAgain = input("Can you play again:- ")
   if playAgain != 'Yes':
      print("Thanku !")
      exit 


else:                     # Quit the game 
    print("Game Ended")
    exit
