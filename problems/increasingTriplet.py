"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such
that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""


def increasingTriplet(nums):
    for i in range(0, len(nums)):
        num = nums[i]
        ls = {}
        ls[i] = num
        for j in range(i+1, len(nums)):
            if nums[j] > num and j > i:
                ls[j] = nums[j]
                num = nums[j]
                if len(ls) == 3:
                    print(ls)
                    return True
    return False

def increasingTriplet2(nums):
    first = float('inf')
    second = float('inf')

    for i in nums:
        if i <= first:
            first = i
        elif i <= second:
            second = i
        else:
            return True

    return False


nums = [1, 2, 3, 4, 5]
nums2 = [0,4,2,1,0,-1,-3]
nums3 = [1,5,0,4,1,3]
print(increasingTriplet2(nums))
print(increasingTriplet2(nums2))
print(increasingTriplet2(nums3))
