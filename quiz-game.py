print("Welcome to an About Me quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Let's play!")
# Score to keep track of points
score = 0

answer = input("Where was I born and raised? ").lower()
if answer == "lawton, ok":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many years did I serve in the U.S. Navy? ").lower()
if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is my favorite color? ").lower()
if answer == "purple":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is my favorite NFL team? ").lower()
if answer == "seahawks":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is my all-time favorite video game? ").lower()
if answer == "gears of war":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

if score == 5:
    print(f"You must be a day one, you got all {score} questions correct!")
elif score == 4:
    print(f"You got a score of {score}, you must be one of my close friends.")
elif score == 3:
    print(f"{score} correct answers... not bad, I guess we can still be cool.")
elif score == 2:
    print(f"Only {score} correct answers.. uhhhh.. yikes.")
elif score == 1:
    print(f"Wow, {score} correct answer, if we were friends, we're not anymore.")
else:
    print(f"You had a score of {score}, Why are you here?")