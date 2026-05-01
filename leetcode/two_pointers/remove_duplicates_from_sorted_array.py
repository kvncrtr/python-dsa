'''
Problem: 
    Given an integer array nums sorted in non-decreasing order, 
    remove the duplicates in-place such that each unique element appears 
    only once. The relative order of the elements should be kept the same.

    Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing 
    duplicates, return the number of unique elements k.

    The first k elements of nums should contain the unique numbers in 
    sorted order. The remaining elements beyond index k - 1 can be ignored.
'''

nums = [0,0,1,1,1,2,2,3,3,4]

def remove_dups(nums):
    i = 1
    
    for j in range(1, len(nums)):
        if nums[j] != nums[i - 1]:
            nums[i] = nums[j]
            i += 1
    return i

remove_dups(nums)