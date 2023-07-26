
x = [5, 6, 9, 2, 33, 1, 34, 56, 10]


def bubbleSortTry(array):
    i = 0
    while i < len(array):
        j = 0
        while j < len(array):
            if array[j] > array[i]:
                aux = array[i]
                array[i] = array[j]
                array[j] = aux
            j += 1
        i += 1


def bubbleSort(arr):
    n = len(arr)
    for i in range(n): #9 iterações
        for j in range(0, n - i - 1): #8 iterações
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

bubbleSort(x)

print(x)



