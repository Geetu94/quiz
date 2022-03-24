print("Welcome to my computer quiz!")
name=input("enter name your name")
print("Welcome____", name)
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Q1. Who is the father of Computer science?	"'\n')
if answer.lower() == "Charles Babbage":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Q2. In a computer, most processing takes place in _______?	"'\n')
if answer.upper() == "CPU":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Q3. Which one is volatile memory in a computer system ?" '\n')
if answer.lower() == "ram":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Q4. One Terabyte (1 TB) is equal to ?" '\n')
if answer.lower() == "1024 gb":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Q5. Scientific Name of Computer?" '\n')
if answer.lower() == "Sillico sapiens":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
