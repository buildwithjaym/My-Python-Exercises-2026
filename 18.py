score = 0

print("Mini Quiz")

answer = input("1. What is 5 + 3? ")

if answer == "8":
    score +=1

answer = input("2. What is the capital of France? ")
if answer.lower() == "paris":
    score +=1

print("Your score:", score, "/2")