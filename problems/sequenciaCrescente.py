def isArrayAsc(arr):
    isAsc = True
    for currentItem in range(0, len(arr), 1):
        for pointer in range(currentItem, len(arr)):
            if arr[currentItem] > arr[pointer]:
                isAsc = False
                break
        if not isAsc:
            break
    return isAsc


if __name__ == '__main__':
    lista1 = [2, 3, 4, 7, 12, 24, 25]
    lista2 = [2, 12, 4, 7, 3, 24, 4]

    print(isArrayAsc(lista1))
    print(isArrayAsc(lista2))


