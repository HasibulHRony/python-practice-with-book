saarc = ["Bangladesh", "Pakistan", "Afghanistan", "Sri Lanka", "Nepal", "Bhutan", "India"]

country = input("Please enter a country name: ")

if country in saarc:
    print(country, "is present in the saarc!", sep=" ")
else:
    print(country, "is not present in the saarc!", sep=" ")

print("Program terminated")