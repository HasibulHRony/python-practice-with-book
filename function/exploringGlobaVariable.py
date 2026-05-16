def myfunc(x):
    print("Inside my func", x)
    x = 10
    print("Inside my func", x)


x = 20
myfunc(x)
print(x)