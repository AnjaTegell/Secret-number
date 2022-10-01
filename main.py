secret = 19
guess = int(input("What is our secret number?: "))

if guess == secret:
    print ("Congratualations, we have a winner! The secret number is " + str(secret) +"!")
else:
    print ("Try again, the number we are looking for is not " + str(guess) + "!")