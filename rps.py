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

game_images = [rock, paper, scissors]
user_choice = int(input(
    "Wanna play rock, paper and scissors? Type 0 for rock, 1 for paper and 2 for scissors\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(
    "Computer choose:")
print(game_images[computer_choice])
# Now to decide who wins the game

if user_choice >= 3 or user_choice < 0:
    print(
        "You choose and invalid number\nYou lose!")
elif user_choice == 0 and computer_choice == 2:
    print(
        "You win!")
elif computer_choice == 0 and user_choice == 2:
    print(
        "You lose!")
elif user_choice > computer_choice:
    print(
        "You win!")
elif computer_choice > user_choice:
    print(
        "You lose!")
elif user_choice == computer_choice:
    print("It's a draw!")


input("press ENTER to exit")
