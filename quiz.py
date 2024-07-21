#Quiz game
print("Welcome to quiz game!!")
player=input("Do you want to play(yes/no)?\n").lower()
if player == "yes":
    print("Let's play")
else:
    exit()
score=0
question1 = input("How many days do we hav in a week?\n").lower()
if question1 == "seven" :
    print("Correct answer")
    score+=1
else:
    print("Wrong answer")
question2 = input("In which direction does the sun rise?\n").lower() 
if question2 == "east" :
    print("Correct answer")
    score+=1
else:
    print("Wrong answer")  
question3 = input("what is our national bird?\n").lower()  
if question3 == "peacock" :
    print("Correct answer")
    score+=1
else:
    print("Wrong answer")     
question4 = input("Which is the fastest animal on the land?\n").lower()  
if question4 == "cheetah" :
    print("Correct answer")
    score+=1
else:
    print("Wrong answer")   
question5 = input("Which is the largest ocean in the world?\n").lower()  
if question5 == "pacific ocean" :
    print("Correct answer")
    score+=1
else:
    print("Wrong answer")   
print(f"Your score is {score}.")
print("Thank you for playing.")