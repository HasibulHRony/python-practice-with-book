# find the greater number from given list
nums = [78, 54, 63, 98, 41, 52, 56]
greater_num = nums[00]
for i in nums:
    if i > greater_num:
        greater_num = i

print("The greater number of the list is: ", greater_num)

# find the smaller number from given list
nums2 = [48, 58, 69, 21, 85, 39,98, 93, 63]
smaller_num = nums2[0]
for i in nums2:
    if smaller_num > i:
        smaller_num = i
print("The smaller number of the list is: ", smaller_num)