def findDuplicates(nums):
    mymap = {}
    duplicados = []
    for i in nums:
        if i in mymap:
            duplicados.append(i)
        else:
            mymap[i] = i
    return duplicados


lista = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(lista))
