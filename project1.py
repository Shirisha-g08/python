import random
rock='''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''




paper ='''
     _______
---'    ___)___
           ______)
          _______)
         _______)
---.__________)
'''


scissors =''' 
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    game_images=[rock,paper,scissors]
    user_choice=int(input("enter your choice: type 0 for rock,1 for paper,2 for scissors."))
    if user_choice>2 or user_choice<0:
        print("invalid.You lose ")
    else:
        print(game_images[user_choice])
        computer_choice=random.randint(0,2)
        print("computer_choice:",game_images[computer_choice])
        if user_choice==computer_choice:
            print("its tie😁")
        elif user_choice==0 and computer_choice==2:
            print("You win!😊")
        elif user_choice==2 and computer_choice==0:
            print("you lose😌")
        elif user_choice>computer_choice:
            print("You win!😊")
        elif user_choice<computer_choice:
            print("You lose😌")

