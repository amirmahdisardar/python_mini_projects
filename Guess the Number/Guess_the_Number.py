# This project is a simple "Guess the Number" game . the user should guess a randomly generated number within a certain range.
# the program have three difficulty levels: easy, medium, and hard. each level determines the range of numbers and the number of attempts allowed.

import random

print("welcome to the 'Guess the Number' game! in range of 1 to 100")
print("choose a difficulty level: easy, medium or hard .")
difficulty = input("enter your choice:").lower()
times_to_guess = 0
if difficulty == "easy":
    times_to_guess = 10
elif difficulty == "medium":
    times_to_guess = 7
elif difficulty == "hard":
    times_to_guess = 5
else:
    print("invalid choice. please enter easy, medium or hard.")

answer = random.randint(1, 100)

for i in range(times_to_guess):
    
    print(f"you have {times_to_guess} attempts to guess the number.")
    
    user_guess = int(input("Enter your guess : "))
    
    if user_guess == answer:
        print(f"congratulations! you guessed the number correctly. the answer was {answer}")
        break
    elif user_guess < answer:
        print("your guess is too low.")
    elif user_guess > answer:
        print("your guess is too high.")
        
    times_to_guess -= 1
    if times_to_guess == 0:
        print(f"you lost !!! the correct answer is {answer}.")
        break
    
