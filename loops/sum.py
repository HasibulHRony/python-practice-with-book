# sum of fifty 1
result = 0
for _ in range(50):
    result = result + 1
print(result)

# sum of first 50 numbers
sum = 0
num = 1
for i in range(50):
    sum = sum + num
    num = num + 1 
print(sum)


# sum of first 50 numbers in some other ways
sum1 = 0
num1 = 0
for i in range(1, 51):
    sum1 = sum1 + num1
    num1 += 1

print(sum1)


# 
sum2 = 0
for num2 in range(1, 51):
    sum2 += num2
print(sum2)

# 
sum3 = 0
for i in range(50):
    sum3 = sum3 + i + 1
print(sum3)

# printing 20 - 30
sum4 = 0
for num4 in range(20, 31):
    sum4 += num4
print(sum4)