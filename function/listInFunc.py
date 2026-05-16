def listFunc(nums):
    nums[0] = 10
    print("Nums in function:", nums)

nums = [88, 56, 53, 62, 65]

print("Befor function call, nums lists =", nums)

listFunc(nums)

print("After function call, nums lists =", nums)