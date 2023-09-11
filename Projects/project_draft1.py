import random


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

user_choice = int(input("Make your choice: Choose 0 for rock, 1 for paper, and 2 for scissors \n"))


computer_choice = random.randint(0,2)
print(f"Computer chose: {computer_choice}")


#game logic 

if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number exiting, and you loose btw! >:(")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 2 and user_choice == 0:
    print("You loose :(")
elif computer_choice == user_choice:
    print("It's a draw!")
elif computer_choice > user_choice:
    print("You loose :(")
elif user_choice > computer_choice:
    print("You win!")
