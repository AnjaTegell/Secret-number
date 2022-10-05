import random

secret = random.randint (1,30)
print ("Pssst, secret is: " + str(secret))

while True:
    guess = int(input("What is our secret number?: "))
    if guess == secret:
        print("Congratualations, we have a winner! The secret number is " + str(secret) + "!")
        break
    elif guess > secret:
        print("Try a smaller number")
    elif guess < secret:
        print("Try a bigger number")
    else:
        print("Try again, the number we are looking for is not " + str(guess) + "!")