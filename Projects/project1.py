rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
game_list = [rock, paper, scissors]


#catch user inputer (remember it's saved as a string by default)
user_choice= int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors. \n"))

if user_choice >=3 or user_choice < 0:
    print("You typed an invalid, you loose! :(")
else:
    print(game_list[user_choice])



    #build random computer choice
    computer_choice = random.randint(0,2)
    print(f"Computer chose: {game_list[computer_choice]} \n")


    #catch index range errors outside of user allowed input

    #for i in range(len(user_choice)):
    #   print(user_choice[i])

    #define computer random choce

    #if user_choice_list > 3: 
    # print("You typed and invalid number, you loose! :(")

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 2 and user_choice == 0:
        print("You loose :(")
    elif computer_choice > user_choice:
        print("You loose :(")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")
