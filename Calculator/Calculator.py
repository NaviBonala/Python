print("Simple Calculator ")

while True:
    num1 = int(input("The first number: "))
    num2 = int(input("The Second number: "))

    print("Select Choice")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    i = int(input("Select your operation: "))

    if i == 1:
        print("Add of two numbers: ", num1 + num2)
    elif i == 2:
        print("Subtract of two numbers: ", num1 - num2)
    elif i == 3:
        print("Multiply of two numbers: ", num1 * num2)
    elif i == 4:
        print("Division of two numbers: ", num1 / num2)
    else:
        print("Wrong Choice")

    again = input("Do you want to do other calculation (yes/no): ").lower()

    if again != "yes":
        print("Thank for using the calculator!!! Goodbye ")
        break
