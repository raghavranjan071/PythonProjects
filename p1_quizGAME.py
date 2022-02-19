print("Welcome to my computer quiz!")
no_of_questions=4
playing=input("Do you want to play? ")
# print(playing)

# if playing != "yes":
#     quit()

if playing.lower() != "yes":      #lower() mmethod converts all strings to lower
    quit()

print("Okay! Let's play :)")
score=0

answer=input("What does CPU stands for? ")
if answer.lower()== "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer=input("What does GPU stands for? ")
if answer.lower()== "graphics processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer=input("What does RAM stands for? ")
if answer.lower()== "random access unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer=input("What does PSU stands for? ")
if answer.lower()== "power supply":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("You got "+ str(score)+ " questions correct! ")
print("You got "+ str((score/no_of_questions) * 100)+ "%.")