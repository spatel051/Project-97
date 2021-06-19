import random

number = random.randint(1, 9)
chances = 0

print("Number Guessing Game")
print("Guess a number (between 1 and 9):")

while chances < 5:
    guess = int(input("Enter you guess:- "))

    if guess == number:
        print("Congratulation you won!!!")
        break

    elif guess < number:
        print("Your guess was too low: Guess a number higher than " + str(guess))
        chances += 1

    else:    
        print("Your guess was too high: Guess a number lower than " + str(guess))
        chances += 1 

if chances == 5 and guess != number:
    print("You lose. The number was " + str(number))