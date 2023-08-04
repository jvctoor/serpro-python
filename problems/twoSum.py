def twoSum(nums, target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            print(numMap)
            return [numMap[complement], i]

        numMap[nums[i]] = i

    return []


print(twoSum([3,2,4], 6))