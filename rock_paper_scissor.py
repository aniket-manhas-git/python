import os
import random
print("***********")
print("*         *")
print("* Welcome *")
print("*         *")
print("***********")
print("Enter any key to start")
input()
os.system('cls')
print("Enter 1 for Rock")
print("2 for Paper")
print("3 for Scissor")
userchoice=input("Enter your choice : ")
userchoice=int(userchoice)
while(not(userchoice>0 and userchoice<4)):
    print("Invalid choice")
    userchoice=input("Enter your choice : ")
    userchoice=int(userchoice)
computer_choice=random.randint(1,3)
if(computer_choice==userchoice):
    print("It's a tie")
elif(computer_choice==1 and userchoice==2):
    print("Computer choose rock and you choose paper")
    print("You win")
elif(computer_choice==2 and userchoice==3):
    print("Computer choose paper and you choose scissor")
    print("You win")
elif(computer_choice==3 and userchoice==1):
    print("Computer choose scissor and you choose rock")
    print("You win")
else:
    print("Computer won")