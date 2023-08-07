def maxOperations(nums, k):
    mp = {}

    for num in nums:
        restante = k - num
        mp[restante] = num

    operations = 0

    for key in mp.keys():
        print("Key: " + str(key))
        while key in nums and mp[key] in nums:
            cont = 0
            if key in nums:
                nums.remove(key)
                cont += 1
            if mp[key] in nums:
                nums.remove(mp[key])
                cont += 1
            if cont == 2:
                operations += 1

    print(nums)
    print(mp)

    return operations


def maxOperations2(nums, k):
    mp = {}
    operations = 0

    for num in nums:
        restante = k - num
        if restante in mp and mp[restante] > 0:
            operations += 1
            mp[restante] -= 1
        else:
            mp[num] = mp.get(num, 0) + 1

    return operations


nums = [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4]
k = 2

print(maxOperations2(nums, k))
