# Author: Mishti Gala
# Email: mishtikalpes@umass.edu
# Date: 1st November 2023

# Print a welcome message to the user.
print("Welcome to the Computer Quiz!")

# Prompt the user to decide whether they want to play the quiz.
playing = input("Do you want to play? ")

# Check if the user's input is not equal to "yes" (case-insensitive).
if playing.lower() != "yes":
    # If the user's response is not "yes," exit the program.
    quit()

# If the user chooses to play, inform them that the game is starting.
print("Okay! Let's play :)")
# Initialize a variable to keep track of the user's score.
score = 0

# Ask the user the first quiz question: "What does CPU stand for?"
answer = input("What does CPU stand for? ")
# Check if the user's answer (converted to lowercase) is correct
if answer.lower() == "central processing unit":
    # If the answer is correct, provide positive feedback and increase the score.
    print("Correct!")
    score += 1
else:
    # If the answer is incorrect, provide feedback to the user.
    print("Incorrect!")

# Repeat the above process for each of the following questions:

# Question 2: "What does GPU stand for?"
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3: "What does RAM stand for?"
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4: "What does CD stand for?"
answer = input("What does CD stand for? ")
if answer.lower() == "compact disk":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 5: "What does OS stand for?"
answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Display the user's final score by printing the number of correct answers.
print("You got " + str(score) + " questions correct!")

# Calculate and display the user's score as a percentage.
# The score is divided by the total number of questions (5) and multiplied by 100.
print("You got " + str((score/5)*100) + "%.")
