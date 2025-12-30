## Write a program that asks for three numbers and prints the largest using a function.

def find_largest(nums):
    if(nums[0] > nums[1] and nums[0] > nums[2]):
        return nums[0]
    elif (nums[1] > nums[2]):
        return nums[1]
    else:
        return nums[2]

nums = []
for i in range(3):
    a = int(input("Enter a number: "))
    nums.append(a)


print(find_largest(nums))
