print("Welcome to my Computer Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay lets play :) ")
score = 0
#question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("incorrect")

#question 2
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("incorrect")

#question 3
answer = input("What does API stand for? ")
if answer.lower() == "application program interface":
    print("Correct")
    score += 1
else:
    print("incorrect")

#question 4
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("incorrect")
    
#question 5
answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct")
    score += 1
else:
    print("incorrect")
    
print("Okay you got " + str(score) + " questions correct")
print("You got " + str((score/4) * 100) + "%")