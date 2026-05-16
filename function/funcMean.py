def funcOfMean(nums):
    sum = 0
    for num in nums:
        sum += num
    mean = sum / len(nums)
    return mean

nums = [88, 53, 64, 72, 81]
average = funcOfMean(nums)
print("Mean of the list's all numbers is:", average)