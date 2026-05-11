year = int(input("Write year:  "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes!", year, "is a leap year!", sep=" ")
        else:
            print("No! The year you enterd", year, "is not leap year!", sep=" ")
    else:
        print("Yes!", year, "is a leap year!", sep=" ")    
else:
    print("No! The year you enterd", year, "is not leap year!", sep=" ")


# another way
if year % 100 != 0 and year % 4 == 0:
    print(year, "is a leap year!")
elif year % 100 == 0 and year % 400 == 0:
    print(year, "is a leap year!")
else:
    print(year, "is not a leap year!")