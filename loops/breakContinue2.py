number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))
terminate = False
while terminate == False:
    operation = input("Please enter add/sub or quit to exit: ")
    if operation == "quit":
        print("You are successfully quit it!")
        terminate = True
        break
    elif operation not in ["add", "sub"]:
        print("Invalid operation")
        continue
    elif operation == "add":
        result = number1 + number2
        print("Summation of these two number is: ", result)
        break
    elif operation == "sub":
        result = number1 - number2
        print("Substraction of these two number is: ", result)
        break