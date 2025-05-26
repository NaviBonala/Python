import random
import string
print("Password Generator ")

while True:


    length = int(input("How many characters do you want in your password: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    print("Here is your password: ", password)

    again = input("Do you want another password (yes/no)").lower()

    if again != "yes":
        print("Thanks for using the Password Generator!!!")
        break