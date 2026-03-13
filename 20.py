import random

number = random.randint(1,20)
attempts = 0

print("Guess the number: (1-20)")


while True:
    guess = int(input("Enter your guess: "))
    attempts +=1

    if guess == number:
        print("Correct! Attempts:", attempts)
        break
    elif guess < number:
        print("Too low")
    elif guess >= 21:
        print("You are out of range")
    else:
        print("Too high")
