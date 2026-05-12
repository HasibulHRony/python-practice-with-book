# find the numbers divideable by 5 among 1 - 100 and also print their sum
sum = 0
divideableNums = []
for i in range(1, 101):
    if i % 5 == 0:
        sum = sum + i
        divideableNums.append(i)

print("The nums are: ", divideableNums, "And the sum of these is: ", sum)