# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
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

images = [rock ,paper ,scissors ]

choice =int(input("What do you choose? Type 0 for rock , 1 for paper and 3 for scissors\n "))
if choice >= 3 or choice <0:
    print("Invalid Number ") 
else:    
    print(images[choice])
    computer_choice = random.randint(0,2)
    print("Computer choose:")
    print(images[computer_choice])



    if choice == 0 and computer_choice == 2:
        print("You Won!")
    elif choice == 2 and computer_choice ==0:
        print("Computer Won!") 

    elif computer_choice > choice:
        print("Computer Won!")
    elif computer_choice < choice:
        print("You Won!")

    elif choice == computer_choice:
        print("Draw!") 

    else:
        print("Invalid Input!!!!!!!!!!!")

#print(f"The Computer choose {computer_choice}")