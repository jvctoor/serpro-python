def findDifference(nums1, nums2):
    arr1 = []
    arr2 = []
    result = []
    for num in nums1:
        if num not in nums2 and num not in arr1:
            arr1.append(num)
    for num in nums2:
        if num not in nums1 and num not in arr2:
            arr2.append(num)
    result.append(arr1)
    result.append(arr2)
    return result
