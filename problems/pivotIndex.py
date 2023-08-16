def pivotIndex(nums):
    for i in range(len(nums)):
        leftSum = 0
        rightSum = 0
        for j in range(0, i + 1):
            leftSum += nums[j]
        for k in range(i, len(nums)):
            rightSum += nums[k]
        if rightSum == leftSum:
            return i
    return -1


