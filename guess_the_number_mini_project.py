# Guess the number
import random
target = random.randint(1,100)
print("You have to guess the number b/w 1 to 100")
while True:
        userchoice = int(input("Guess the target or Quit"))
        if(userchoice == "Quit"):
                break
        elif(userchoice == target):
                print("Success : Correct Guess!!!")
                break
        elif(userchoice < target):
                print("Your number was too small. Take a bigger guess...")
        else:
                print("Your number was too big. Take a smaller guess...")
print("____GAME OVER____")