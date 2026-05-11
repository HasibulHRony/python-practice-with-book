number = input("Please enter a number: ")
number = int(number)

if number < 0:
    print(number, " is negative!")
elif number > 0:
    print(number, " is positive!")
else:
    print("You enterd ",number, "! ", number, " is nither positive nor negative!", sep="")