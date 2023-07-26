

x = [5, 6, 9, 2, 33, 1, 34, 56, 10]
y = [5, 6, 9, 2, 33, 1, 34, 56, 10]


def selectionSortTry(arr):
    n = len(arr)
    for currentItem in range(n):
        currentMinItem = currentItem
        for j in range(currentItem+1, n):
            if arr[j] < arr[currentMinItem]:
                currentMinItem = j
        aux = arr[currentItem]
        arr[currentItem] = arr[currentMinItem]
        arr[currentMinItem] = aux


def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        currentMinItem = i
        for j in range(i + 1, n):
            if arr[j] < arr[currentMinItem]:
                currentMinItem = j
        arr[i], arr[currentMinItem] = arr[currentMinItem], arr[i]


selectionSortTry(x)
selectionSort(y)
print(f'Meu: {x}')
print(f'GPT: {y}')