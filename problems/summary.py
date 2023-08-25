def summaryRanges(nums):
    ranges = []
    i = 0
    while i < len(nums):
        rangex = []
        pointer = i + 1
        if pointer >= len(nums):
            rangex.append(nums[i])
            ranges.append(str(rangex[0]))
            i += 1
            continue
        soma = 1
        while nums[pointer] == nums[i] + soma:
            pointer += 1
            soma += 1
            if pointer >= len(nums):
                break
        rangex.append(nums[i])
        rangex.append(nums[pointer - 1])
        if rangex[0] == rangex[1]:
            ranges.append(str(rangex[0]))
        else:
            ranges.append(str(rangex[0]) + "->" + str(rangex[1]))
        i = pointer

    return ranges