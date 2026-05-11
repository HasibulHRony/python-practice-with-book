number = 30

print(number > 40)
print(number < 40)
print(number > 20 and number < 100)
print(number > 20 and number > 100)
print(number < 20 and number > 100)
print(number > 20 or number < 100)
print(number < 20 or number < 100)
print(number > 20 or number > 100)

today = "monday"
time = 4

if today != "monday" and time < 4:
    print("You Can go to Nilkhet!")
else:
    print("All shop are closed! You should not go!")