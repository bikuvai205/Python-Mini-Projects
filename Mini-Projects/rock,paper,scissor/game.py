# Welcome to the classic game of Rock,Paper and Scissor 
# Choose the option for your choice as:
# 1 = Rock
# 2 = Paper
# 3 = Scissor
# Rules:
# Rock beats Scissor
# Paper beats Rock 
# Scissor beats Paper 
#---------Good Luck---------

import random

lists = ["Rock","Paper","Scissor"]

print("---------Choose the following----")
print('''# 1 = Rock
# 2 = Paper
# 3 = Scissor
 ---------Good Luck---------''')
flag = True
while(flag):
    computer_choice = random.choice(lists)
    human_choice = int(input("Enter your choice :"))
    
    if(human_choice == 1):
        if (computer_choice == "Rock"):
          print("Draw ! You both choosed Rock")
        elif( computer_choice == "Paper"):
          print("Opps,You lost. The computer choosed Paper")
        else:
          print("Yayy! You win. The computer choosed Scissor")
    elif(human_choice == 2):
        if (computer_choice == "Rock"):
          print("Yayy! You win. The computer choosed Rock")
        elif( computer_choice == "Paper"):
          print("Draw ! You both choosed Paper")
        else:
          print("Opps,You lost. The computer choosed Scissor")
    else:
        if (computer_choice == "Rock"):
          print("Opps,You lost. The computer choosed Rock")
        elif( computer_choice == "Paper"):
          print("Yayy! You win. The computer choosed Paper")
        else:
          print("Draw ! You both choosed Scissor")
    
   
    game_continue = input("Do you want to continue?y/n:")

    if game_continue == "n":
       flag = False
       print("--------Thankyou for playing!!!---------")
   

