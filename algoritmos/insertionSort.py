
x = [5, 6, 9, 2, 33, 1, 34, 56, 10]


def insertionSortTry(arr):
    n = len(arr)
    for i in range(n):
        if i == 0:
            continue
        for j in range(i):
            if arr[j] > arr[i]:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


insertionSort(x)
print(x)

