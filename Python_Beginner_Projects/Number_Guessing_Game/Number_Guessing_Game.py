import random

secret_number = random.randint(0, 100)
guess = int(input("Guess a number from the range of 0 and 100:  "))

while guess != secret_number:
    if guess < secret_number:
        print('Too Low')
    else:
        print('Too High')
    guess = int(input("Try again...: "))

print("Congratulations! You guessed it right!!!")