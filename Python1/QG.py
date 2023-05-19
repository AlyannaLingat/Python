"""
class Point():
    def __init__(self, input1, input2):
        self.x=input1
        self.y=input2
p=Point(10,18)
print(p.x)
print(p.y)
"""
"""
print("======== Welcome to Quiz Game!!!=======")
print("---------------------------------------")

def quiz_game(question,answer):
    global score
    guissing = True
    while guissing < 3:
        if question() == answer():
            print("Correct Answer")
            score = score + 10
            quessing = False
        else:
            question = input("Sorry Wrong Answer")

score = 0
print("Choose the Correct Answer!!")
question1 = input("What is the real name of Iron Man? ")
print("A. Tony Stark")
print("B. Steve Roger")
print("C. Nick Furry")
print("D. Bruce Banner")
quiz_game(question1, "A")
print("Your Score is " + str (score))
"""

"""
print("======== Welcome to Quiz Game!!!=======")
print("---------------------------------------")
score = 0

print("what is your name?")
name = input("Name: ")
print(f"Hi, Mr/Ms. {name}, Welome to Marvel Quiz Game! You will be answer 5 questions.")
print(f"Every question has a 10 points. Good luck Mr/Ms. {name}")
enter = input("Press Enter if you want to continue. ")



print("Choose the Correct Answer")
print("Question 1")
print("What is the real name of Iron Man? ")
print("A. Tony Stark")
print("B. Steve Roger")
print("C. Nick Furry")
print("D. Bruce Banner")
answer1 = ("A") 
answer1 = ("a")
prob1 = input("> ")

if (prob1 == answer1):
    print("Correct Answer")
    score = score + 10
else:
    print("Your answer is wrong")
    
print("Your current score is " + str(score) )
print("Question 2")
print("What is the name of Thor's Hammer? ")
print("A. Vanir")
print("B. Aesir")
print("C. Mjolnir")
print("D. Norn")
answer2 = ("C")
answer2 = ("c")
prob2 = input("> ")
if (prob2 == answer2):
    print("Correct Answer")
    score = score + 10
else:
    print("Your answer is wrong")
    

print("Your current score is " + str(score) )
print("Question 3")
print("Before becoming Vision, what is the name of Iron Man’s A.I. butler? ")
print("A. H.O.M.E.R.")
print("B. J.A.R.V.I.S.")
print("C. A.L.F.R.E.D.")
print("D. M.A.R.V.I.N.")
answer3 = ("B")
answer3 = ("b")
prob3 = input("> ")
if (prob3 == answer3):
    print("Correct Answer")
    score = score + 10
else:
    print("Your answer is wrong")
    
    
print("Your current score is " + str(score) )
print("Question 4")
print("What is the real name of the Black Panther? ")
print("A. M’Baku")
print("B. N’Jadaka")
print("C. N’Jobu")
print("D. T’Challa")
answer4 = ("D")
answer4 = ("d")
prob4 = input("> ")
if (prob4 == answer4):
    print("Correct Answer")
    score = score + 10
else:
    print("Your answer is wrong")
   
print("Your current score is " + str(score) )
print("Question 5")
print("Who does the Mad Titan sacrifice to acquire the Soul Stone? ")
print("A. Ebony Maw")
print("B. Cull Obsidian")
print("C. Gamora")
print("D. Cull Obsidian")
answer5 = ("C")
answer5 = ("c")
prob5 = input("> ")
if prob5 == (answer5):
    print("Correct Answer")
    score = score + 10
else:
    print("Your answer is wrong")
    
print("Your current score is " + str(score) )

print(f"Your Total Score is " + str (score) + " out of 50 ")
"""

print(" Bus Seats Reservation ")
rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')


    
