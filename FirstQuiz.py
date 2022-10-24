#Set up
score = 0
print("Welcome to my 'Why do you know that' quiz!\n")
name = input("What is your name? ")
print("Hello", name)
ready = input("Are you ready? ").lower()

if ready == "yes":
    print("Let's Start")
else:
    print("See ya later")
    exit()

print("Your score is", score)

#QUESTION 1
print("\n\nQuestion 1")
ans1 = input("What planet is closest to the Sun? ").lower()

if ans1 == "mercury":
    print("CORRECT!")
    score += 1

else:
    print("Sorry, the correct answer was Mercury")

print("Your score is", score)

#QUESTION 2
print("\n\nQuestion 2")
ans2 = int(input("How many continents are there? (number only) "))

if ans2 == 7:
    print("CORRECT!")
    score += 1

else:
    print("Sorry, the correct answer was 7")

print("Your score is", score)

#QUESTION 3
print("\n\nQuestion 3")
ans3 = input("What state is the NFL Hall of Fame located? ").lower()

if ans3 == "ohio":
    print("CORRECT!")
    score += 1

else:
    print("Sorry, the correct answer was Ohio")

print("Your score is", score)

#QUESTION 4
print("\n\nQuestion 4")
ans4 = int(
    input("What is the total number of dots on a standard PAIR of dice? "))

if ans4 == 42:
    print("CORRECT!")
    score += 1

else:
    print("Sorry, the correct answer was 42")

print("Your score is", score)

#QUESTION 5
print("\n\nQuestion 5")
ans5 = input("What is the chemical symbol of Potassium? ").lower()

if ans5 == "k":
    print("CORRECT!")
    score += 1
else:
    print("Sorry, the correct answer was K")

print("Your score is", score)

#KEEP PLAYING?
while True:
    keep_going = input("\n\nWould you like to keep going? ").lower()
    if keep_going == "yes":
        print("\n\nOkay!")
        break
    elif keep_going == "no":
        print("\nOkay\nThank you for playing!\n")
        final_score = ((float(score) / 5) * 100)
        print("Your final score was", final_score, "%")
        exit()
    else:
        print("You have made an invalid choice, please try again")

#QUESTION 6
print("\n\nQuestion 6")
ans6 = input("What country did Ikea originate in? ").lower()

if ans6 == "sweden":
    print("CORRECT!")
    score += 1
else:
    print("Sorry, the correct answer was Sweden")

print("Your score is", score)

#QUESTION 7
print("\n\nQuestion 7")
ans7 = int(
    input(
        "Which U.S. Constitution Amendment established Prohibition (number only) "
    ))

if ans7 == 18:
    print("CORRECT!")
    score += 1
else:
    print("Sorry, the correct answer was 18")

print("Your score is", score)

#QUESTION 8
print("\n\nQuestion 8")
ans8 = input("True of False:  There are 5,820ft in a mile? ").lower()

if ans8 == "true":
    print("CORRECT!")
    score += 1
else:
    print("Sorry, the correct answer was True")

print("Your score is", score)

#QUESTION 9
print("\n\nQuestion 9")
ans9 = int(input("How many defensive players are on a baseball field? "))

if ans9 == 9:
    print("CORRECT!")
    score += 1
else:
    print("Sorry, the correct answer was 9")

print("Your score is", score)

#QUESTION 10
print("\nFinal Question")
while True:
    ans10 = input("\nWas this the best quiz you've ever played? ").lower()
    if ans10 == "yes":
        print("\n\nCORRECT!")
        score += 1
        break
    elif ans10 == "no":
        print("\nwrong...")
        break
    else:
        print("\nYou have made an invalid choice, please try again")

print("\n\nThank you for playing!")

final_score = ((float(score) / 10) * 100)
print("Your final score was", final_score, "%")
