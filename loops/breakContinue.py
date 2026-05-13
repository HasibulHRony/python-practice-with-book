while True:
    n = int(input("Please enter number (0 to exit): "))
    if n < 0:
        print("We only allow positive numberl. Please try again.")
        continue
    if n == 0:
        break
    print("Square of", n, "is", n*n)